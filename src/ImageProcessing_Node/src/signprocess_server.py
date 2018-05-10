#!/usr/bin/env python
# -*-coding:utf-8-*-
from ImageProcessing_Node.msg import DetectSignAction, DetectSignGoal, DetectSignResult, DetectSignFeedback
from cv_bridge import CvBridge
import numpy as np
import os
import actionlib
import cv2
import rospy


class SignProcessServer:
    def __init__(self):
        self.dir_path, self.compare_img = self.fn_load()

        # 특징점 매칭에 필요한 기본 변수들
        self.src_kp = None
        self.src_des = None
        self.kp = dict(kp1=[], kp2=[], kp3=[], kp4=[])
        self.des = dict(des1=[], des2=[], des3=[], des4=[])
        self.matches = dict(match1=[], match2=[], match3=[], match4=[])
        self.good = dict(good1=[], good2=[], good3=[], good4=[])

        # 특징점 매칭을 위한 기본 설정들
        self.sift = cv2.xfeatures2d.SIFT_create()
        self.flann = self.fn_flann_init()

        # 외부에서 이미지를 받아오는 설정
        self.cvb = CvBridge()
        self.act_sign = actionlib.SimpleActionServer('/image/controller/sign', DetectSignAction, self.do_goal, False)
        self.act_sign.start()

    def do_goal(self, goal):
        if self.act_sign.is_preempt_requested():
            result = DetectSignResult()
            result.result = False
            self.act_sign.set_preempted(result, "Detection completed successfully!")
            return

        frame = self.cvb.imgmsg_to_cv2(goal.sign_img, "bgr8")
        if self.dir_path is None:
            rospy.logerr("No such file was found!")
            exit()

        result_img = None
        data_dict = dict()
        self.src_kp, self.src_des = self.sift.detectAndCompute(frame, None)
        for key in self.compare_img.keys():
            if key == 'traffic':
                self.matches['match1'] = self.flann.knnMatch(self.src_des, self.des['des1'], k=2)
                data_dict = dict(kp='kp1', mkey='match1', gkey='good1', num=1)
            elif key == 'parking':
                self.matches['match2'] = self.flann.knnMatch(self.src_des, self.des['des2'], k=2)
                data_dict = dict(kp='kp2', mkey='match2', gkey='good2', num=2)
            elif key == 'crossbar':
                self.matches['match3'] = self.flann.knnMatch(self.src_des, self.des['des3'], k=2)
                data_dict = dict(kp='kp3', mkey='match3', gkey='good3', num=3)
            elif key == 'tunnel':
                self.matches['match4'] = self.flann.knnMatch(self.src_des, self.des['des4'], k=2)
                data_dict = dict(kp='kp4', mkey='match4', gkey='good4', num=4)
            else:
                rospy.logerr("Wrong key value!")
                exit()

            for m, n in self.matches[data_dict['mkey']]:
                if m.distance < 0.6 * n.distance:
                    self.good[data_dict['gkey']].append(m)
            if len(self.good[data_dict['gkey']]) > 7:
                src_pts = np.float32([self.src_kp[m.queryIdx].pt for m in self.good[data_dict['gkey']]]).reshape(-1, 1, 2)
                dst_pts = np.float32([self.kp[data_dict['kp']][m.trainIdx].pt for m in self.good[data_dict['gkey']]]).reshape(-1, 1, 2)

                M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
                matches_mask = mask.ravel().tolist()

                mse = self.fn_calc_mse(src_pts, dst_pts)
                if mse < 40000:
                    rospy.loginfo(key + " Sign Detect")
                    draw_params = dict(matchColor=(0, 0, 255), singlePointColor=None, matchesMask=matches_mask, flags=2)
                    result_img = cv2.drawMatches(frame, self.src_kp, self.compare_img[key], self.kp[data_dict['kp']],
                                                 self.good[data_dict['gkey']], None, **draw_params)
                    msg = True
                else:
                    msg = False
            else:
                matches_mask = None
                msg = False

            feedback = DetectSignFeedback()
            feedback.status = str(msg)
            feedback.detect_num = data_dict['num']
            self.act_sign.publish_feedback(feedback)

        if result_img is None:
            pass
        else:
            cv2.imshow("Result", result_img)
            cv2.waitKey(1)
        self.fn_clear()

        result = DetectSignResult()
        result.result = 'Finish'
        self.act_sign.set_succeeded(result, "Detection completed successfully!")

    @staticmethod
    def fn_load():
        dir_path = os.path.realpath(os.path.dirname(__file__))
        dir_path = dir_path.replace('ImageProcessing_Node/src', 'ImageProcessing_Node/data')

        compare_image = dict(traffic=cv2.imread(dir_path + "/card1.jpg"),
                             parking=cv2.imread(dir_path + "/card2.jpg"),
                             crossbar=cv2.imread(dir_path + "/card3.jpg"),
                             tunnel=cv2.imread(dir_path + "/card4.jpg"))
        return dir_path, compare_image

    def fn_flann_init(self):
        for key in self.compare_img.keys():
            if key == 'traffic':
                self.kp['kp1'] = self.sift.detectAndCompute(self.compare_img[key], None)[0]
                self.des['des1'] = self.sift.detectAndCompute(self.compare_img[key], None)[1]
            elif key == 'parking':
                self.kp['kp2'] = self.sift.detectAndCompute(self.compare_img[key], None)[0]
                self.des['des2'] = self.sift.detectAndCompute(self.compare_img[key], None)[1]
            elif key == 'crossbar':
                self.kp['kp3'] = self.sift.detectAndCompute(self.compare_img[key], None)[0]
                self.des['des3'] = self.sift.detectAndCompute(self.compare_img[key], None)[1]
            elif key == 'tunnel':
                self.kp['kp4'] = self.sift.detectAndCompute(self.compare_img[key], None)[0]
                self.des['des4'] = self.sift.detectAndCompute(self.compare_img[key], None)[1]
            else:
                return

        FLANN_INDEX_KDTEE = 0
        index_params = dict(algorithm=FLANN_INDEX_KDTEE, trees=5)
        search_params = dict(checks=50)
        return cv2.FlannBasedMatcher(index_params, search_params)

    def fn_clear(self):
        for i in range(1, 5):
            self.good['good' + str(i)] = []

    @staticmethod
    def fn_calc_mse(src_pts, dst_pts):
        squared_diff = (src_pts - dst_pts) ** 2
        sum = np.sum(squared_diff)
        num_all = src_pts.shape[0] * src_pts.shape[1]
        err = sum / num_all
        return err

    @staticmethod
    def main():
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node("SignProcessing_Node")
    node = SignProcessServer()
    node.main()

