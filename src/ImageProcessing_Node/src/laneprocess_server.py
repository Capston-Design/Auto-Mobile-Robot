#!/usr/bin/env python
# -*-coding:utf-8-*-
from ImageProcessing_Node.src.image_processor import ImageProcessor
from std_msgs.msg import Float32
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge
import numpy as np
import cv2
import rospy


class LaneProcessServer:
    def __init__(self):
        self.bridge = CvBridge()
        self.twist = Twist()
        self.ip = ImageProcessor()

        self.is_perspective = True
        self.center_x = 392
        self.center_y = 370
        self.gap_pre = 200
        self.cx_pre = 392

        self.list_pos_pre, self.list_pos = [], []
        self.list_right_pts_x, self.list_right_pts_y = [], []
        self.list_left_pts_x, self.list_left_pts_y = [], []

        self.image_sub = rospy.Subscriber('/image_raw', Image, self.image_callback)
        self.error_pub = rospy.Publisher('error', Float32, queue_size=1)

    def init_list_pts(self):
        self.list_right_pts_x = []
        self.list_right_pts_y = []
        self.list_left_pts_x = []
        self.list_left_pts_y = []

    def image_callback(self, msg):
        img_ori = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        if self.is_perspective:
            self.list_pos_pre, self.list_pos = self.ip.perspective_transform(img_ori)

        val_ori_h, val_ori_w = img_ori.shape[:2]
        arr_pos_pre = np.float32(self.list_pos_pre)
        arr_pos = np.float32(self.list_pos)
        mat_perspective = cv2.getPerspectiveTransform(arr_pos_pre, arr_pos)
        img_trans = cv2.warpPerspective(img_ori, mat_perspective, (int(val_ori_w * 1.2), val_ori_h * 2))

        mask_line = self.ip.hsv_filter(img_trans)
        line = cv2.bitwise_and(img_trans, img_trans, mask=mask_line)

        # threshold
        img_gray = cv2.cvtColor(line, cv2.COLOR_BGR2GRAY)
        _, img_threshold = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)
        img_threshold = cv2.morphologyEx(img_threshold, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
        img_threshold = cv2.morphologyEx(img_threshold, cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8))

        val_threshold_h, val_threshold_w = img_threshold.shape[:2]
        num_of_section = int(val_threshold_h / 4)
        val_section_h = int(val_threshold_h / num_of_section)

        self.init_list_pts()

        for n_section in range(num_of_section):
            section_top = val_section_h - (n_section + 1) * val_section_h
            img_section = img_threshold[section_top:section_top + val_section_h, :]

            if np.count_nonzero(img_section) > 10:
                moment = cv2.moments(img_section)
                if moment['m00'] > 0:
                    xmid = int(moment['m10'] / moment['m00'])
                img_section_left = img_section[:, :xmid]
                img_section_right = img_section[:, xmid:]

                cy = int(section_top + val_section_h / 2)

                if img_threshold[cy, xmid] == 255 or img_trans[cy, xmid, :] == np.array([0, 0, 0]):
                    if np.count_nonzero(img_section) > 25:
                        cx = int(xmid)
                        if xmid > self.cx_pre:
                            self.list_right_pts_x.append(cx)
                            self.list_right_pts_y.append(cy)
                            cv2.circle(img_trans, (cx, cy), 8, (0, 255, 0), 2)
                            self.cx_pre = cx - self.gap_pre
                        else:
                            self.list_left_pts_x.append(cx)
                            self.list_left_pts_y.append(cy)
                            cv2.circle(img_trans, (cx, cy), 8, (0, 0, 255), 2)
                            self.cx_pre = cx + self.gap_pre

                else:
                    if np.count_nonzero(img_section_left) > 25 and np.count_nonzero(img_section_right) > 25:
                        moment_left = cv2.moments(img_section_left)
                        if moment_left['m00'] > 0:
                            cx1 = int(moment_left['m10'] / moment_left['m00'])
                        else:
                            cx1 = int(xmid)

                        moment_right = cv2.moments(img_section_right)
                        if moment_right['m00'] > 0:
                            cx2 = int(xmid + moment_right['m10'] / moment_right['m00'])
                        else:
                            cx2 = int(xmid)

                        self.list_left_pts_x.append(cx1)
                        self.list_left_pts_y.append(cy)
                        self.list_right_pts_x.append(cx2)
                        self.list_right_pts_y.append(cy)
                        cv2.circle(img_trans, (cx1, cy), 8, (0, 0, 255), 2)
                        cv2.circle(img_trans, (cx2, cy), 8, (0, 255, 0), 2)
                        cv2.circle(img_trans, (xmid, cy), 8, (0, 255, 255), 2)
                        self.cx_pre = int((cx1 + cx2) / 2)

        arr_y = np.linspace(0, val_threshold_h - 1, val_threshold_h)
        if len(self.list_left_pts_x) > 50 and len(self.list_right_pts_x) > 50:
            try:
                list_left_lane_fit = np.polyfit(self.list_left_pts_y, self.list_left_pts_x, 2)
                arr_left_x = list_left_lane_fit[0] * arr_y ** 2 + list_left_lane_fit[1] * arr_y + list_left_lane_fit[2]
                arr_pts = np.array([np.transpose(np.vstack([arr_left_x, arr_y]))])
                cv2.polylines(img_trans, np.int_([arr_pts]), isClosed=False, color=(255, 0, 255), thickness=5)

                list_right_lane_fit = np.polyfit(self.list_right_pts_y, self.list_right_pts_x, 2)
                arr_right_x = list_right_lane_fit[0] * arr_y ** 2 + list_right_lane_fit[1] * arr_y + list_right_lane_fit[2]
                arr_pts = np.array([np.transpose(np.vstack([arr_right_x, arr_y]))])
                cv2.polylines(img_trans, np.int_([arr_pts]), isClosed=False, color=(255, 255, 0), thickness=5)

                arr_x = np.mean([arr_left_x, arr_right_x], axis=0)
                arr_pts = np.array([np.transpose(np.vstack([arr_x, arr_y]))])
                cv2.polylines(img_trans, np.int_([arr_pts]), isClosed=False, color=(255, 0, 0), thickness=5)

                self.gap_pre = int(abs(arr_right_x[self.center_y] - arr_x[self.center_y]))
            except Exception as e:
                rospy.logerr("Fail.1 : " + e)
                return

        elif len(self.list_left_pts_x) > 50 and len(self.list_right_pts_x) <= 50:
            try:
                list_left_lane_fit = np.polyfit(self.list_left_pts_y, self.list_left_pts_x, 2)
                arr_left_x = list_left_lane_fit[0] * arr_y ** 2 + list_left_lane_fit[1] * arr_y + list_left_lane_fit[2]
                arr_pts = np.array([np.transpose(np.vstack([arr_left_x, arr_y]))])
                cv2.polylines(img_trans, np.int_([arr_pts]), isClosed=False, color=(255, 0, 255), thickness=5)

                arr_x = np.add(arr_left_x, self.gap_pre)
                arr_pts = np.array([np.transpose(np.vstack([arr_x, arr_y]))])
                cv2.polylines(img_trans, np.int_([arr_pts]), isClosed=False, color=(255, 0, 0), thickness=5)
            except Exception as e:
                rospy.logerr("Fail.2 : " + e)
                return

        elif len(self.list_left_pts_x) <= 50 and len(self.list_right_pts_x) > 50:
            try:
                list_right_lane_fit = np.polyfit(self.list_right_pts_y, self.list_right_pts_x, 2)
                arr_right_x = list_right_lane_fit[0] * arr_y ** 2 + list_right_lane_fit[1] * arr_y + list_right_lane_fit[2]
                arr_pts = np.array([np.transpose(np.vstack([arr_right_x, arr_y]))])
                cv2.polylines(img_trans, np.int_([arr_pts]), isClosed=False, color=(255, 255, 0), thickness=5)

                arr_x = np.subtract(arr_right_x, self.gap_pre)
                arr_pts = np.array([np.transpose(np.vstack([arr_x, arr_y]))])
                cv2.polylines(img_trans, np.int_([arr_pts]), isClosed=False, color=(255, 0, 0), thickness=5)
            except Exception as e:
                rospy.logerr("Fail.3 : " + e)
                return

        else:
            rospy.logerr("Lane not found")
            cv2.imshow('img', img_ori)
            cv2.imshow('trans', img_trans)
            cv2.imshow('threshold', img_threshold)
            return

        if self.is_perspective:
            self.center_x = arr_x[self.center_y]
            self.is_perspective = False

        self.cx_pre = arr_x[self.center_y]
        err = arr_x[self.center_y] - self.center_x
        self.error_pub.publish(err)
        rospy.loginfo("Error : " + str(err))

        # Test Code
        # cv2.imshow('img', img_ori)
        # cv2.imshow('trans', img_trans)
        # cv2.imshow('threshold', img_threshold)
        # cv2.waitKey(1)

    @staticmethod
    def main():
        rospy.spin()


if __name__ == '__main__':
    rospy.init_node("LaneProcessing_Node")
    node = LaneProcessServer()
    node.main()
