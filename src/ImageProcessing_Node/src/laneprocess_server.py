#!/usr/bin/env python
# -*-coding:utf-8-*-
from image_processor import ImageProcessor
from std_msgs.msg import Float32
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy as np
import cv2
import rospy


class LaneProcessServer:
    def __init__(self):
        self.bridge = CvBridge()

        self.list_pos_ori = rospy.get_param('/perspective/original', [[220, 0], [0, 240], [460, 0], [680, 240]])
        self.list_pos_trans = rospy.get_param('/perspective/trans', [[212, 0], [212, 480], [620, 0], [620, 480]])
        self.center_x, self.center_y = rospy.get_param('/perspective/center', [392, 370])
        #rospy.loginfo(self.list_pos_ori)
        #rospy.loginfo(self.list_pos_trans)
        #rospy.loginfo(self.center_x)
        #rospy.loginfo(self.center_y)
        #rospy.loginfo(type(self.list_pos_ori))
        #rospy.loginfo(type(self.list_pos_trans))
        #rospy.loginfo(type(self.center_x))
        #rospy.loginfo(type(self.center_y))

        self.shift_pre = 200
        self.gap_pre = 400
        self.cx_left_pre = 192
        self.cx_right_pre = 592

        self.list_right_pts_x, self.list_right_pts_y = [], []
        self.list_left_pts_x, self.list_left_pts_y = [], []

        self.image_sub = rospy.Subscriber('/image/controller/lane', Image, self.image_callback)
        #self.image_sub = rospy.Subscriber('/image_raw', Image, self.image_callback)
        self.error_pub = rospy.Publisher('/error/image_processor/lane', Float32, queue_size=1)

    def init_list_pts(self):
        self.list_right_pts_x = []
        self.list_right_pts_y = []
        self.list_left_pts_x = []
        self.list_left_pts_y = []

    def image_callback(self, msg):
        img_ori = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        #img_ori2 = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        #img_ori = img_ori2[240:, :].copy()
        img_trans = ImageProcessor.trans_perspective(img_ori, self.list_pos_ori, self.list_pos_trans)

        mask_line = ImageProcessor.hsv_filter(img_trans)
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
            section_top = val_threshold_h - (n_section + 1) * val_section_h
            img_section = img_threshold[section_top:section_top + val_section_h, :]
            list_section = []

            cy = int(section_top + val_section_h / 2)
            if np.count_nonzero(img_section) <= 10: continue

            moment = cv2.moments(img_section)
            if moment['m00'] > 0:
                xmid = int(moment['m10'] / moment['m00'])
            else :
                xmid = 384
            x0 = 0
            list_section.append((img_section, x0, xmid))

            count = 0
            find_all_section = True
            while find_all_section:
                count += 1
                #print(count)
                find_all_section = False
                list_section_new = []
                for (img_section, x0, xmid) in list_section:
                    #if img_threshold[cy, x0+xmid] == 255 or img_trans[cy, x0+xmid, 0] == 0:
                    if img_threshold[cy, x0+xmid] == 255:
                        list_section_new.append((img_section, x0, xmid))
                    else:
                        img_section_left = img_section[:, :xmid]
                        img_section_right = img_section[:, xmid:]
                        cv2.circle(img_trans, (xmid, cy), 8, (0, 255, 255), 2)

                        if np.count_nonzero(img_section_left) > 10:
                            moment = cv2.moments(img_section_left)
                            if moment['m00'] > 0:
                                xmid_left = int(moment['m10'] / moment['m00'])
                                x0_left = x0
                                list_section_new.append((img_section_left, x0_left, xmid_left))
                                find_all_section = True

                        if np.count_nonzero(img_section_right) > 10:
                            moment = cv2.moments(img_section_right)
                            if moment['m00'] > 0:
                                xmid_right = int(moment['m10'] / moment['m00'])
                                x0_right = x0 + xmid
                                list_section_new.append((img_section_right, x0_right, xmid_right))
                                find_all_section = True

                list_section = list_section_new
                if count > 5:
                    print("over")
                    break

            if len(list_section) >= 2:
                list_left_gap = []
                list_right_gap = []
                for (img_section, x0, xmid) in list_section:

                    list_left_gap.append(abs(self.cx_left_pre - (x0 + xmid)))
                    list_right_gap.append(abs(self.cx_right_pre - (x0 + xmid)))

                list_left_right_gap = list_left_gap + list_right_gap
                idx_left_right = list_left_right_gap.index(min(list_left_right_gap))
                val_first_min = min(list_left_right_gap)
                #val_second_min = 0

                if idx_left_right < len(list_section):
                    idx_left = idx_left_right
                    list_right_gap[idx_left] = 10000
                    idx_right = list_right_gap.index(min(list_right_gap))
                    val_second_min = min(list_right_gap)
                else:
                    idx_right = idx_left_right - len(list_section)
                    list_left_gap[idx_right] = 10000
                    idx_left = list_left_gap.index(min(list_left_gap))
                    val_second_min = min(list_left_gap)

                if val_first_min < 160:
                    if val_second_min < 160:
                        cx_left = list_section[idx_left][1] + list_section[idx_left][2]
                        cx_right = list_section[idx_right][1] + list_section[idx_right][2]

                        self.cx_left_pre = cx_left
                        self.cx_right_pre = cx_right
                        self.gap_pre = cx_right - cx_left

                        self.list_left_pts_x.append(cx_left)
                        self.list_left_pts_y.append(cy)
                        self.list_right_pts_x.append(cx_right)
                        self.list_right_pts_y.append(cy)
                        cv2.circle(img_trans, (cx_left, cy), 8, (0, 0, 255), 2)
                        cv2.circle(img_trans, (cx_right, cy), 8, (0, 255, 0), 2)
                    else:
                        if idx_left_right < len(list_section):
                            cx = list_section[idx_left][1] + list_section[idx_left][2]
                            self.cx_left_pre = cx
                            self.cx_right_pre = cx + self.gap_pre
                            self.list_left_pts_x.append(cx)
                            self.list_left_pts_y.append(cy)
                            cv2.circle(img_trans, (xmid, cy), 8, (0, 0, 255), 2)
                        else:
                            cx = list_section[idx_right][1] + list_section[idx_right][2]
                            self.cx_right_pre = cx
                            self.cx_left_pre = cx - self.gap_pre
                            self.list_right_pts_x.append(cx)
                            self.list_right_pts_y.append(cy)
                            cv2.circle(img_trans, (cx, cy), 8, (0, 255, 0), 2)

            elif len(list_section) == 1:
                [(img_section, x0, xmid)] = list_section
                cx = x0 + xmid
                left_gap = abs(self.cx_left_pre - cx)
                right_gap = abs(self.cx_right_pre - cx)

                if left_gap < right_gap:
                    cx = x0 + xmid
                    self.cx_left_pre = cx
                    self.cx_right_pre = cx + self.gap_pre
                    self.list_left_pts_x.append(cx)
                    self.list_left_pts_y.append(cy)
                    cv2.circle(img_trans, (xmid, cy), 8, (0, 0, 255), 2)
                else:
                    cx = x0 + xmid
                    self.cx_right_pre = cx
                    self.cx_left_pre = cx - self.gap_pre
                    self.list_right_pts_x.append(cx)
                    self.list_right_pts_y.append(cy)
                    cv2.circle(img_trans, (cx, cy), 8, (0, 255, 0), 2)

        #print(self.list_left_pts_x)
        #print(self.list_left_pts_y)
        #print(self.list_right_pts_x)
        #print(self.list_right_pts_y)

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

                self.shift_pre = int(abs(arr_right_x[self.center_y] - arr_x[self.center_y]))
                self.cx_left_pre = int(arr_left_x[self.center_y])
                self.cx_right_pre = int(arr_right_x[self.center_y])
                self.gap_pre = self.shift_pre * 2
            except Exception as e:
                rospy.logerr("Fail.1 : " + e)
                return

        elif len(self.list_left_pts_x) > 50 and len(self.list_right_pts_x) <= 50:
            try:
                list_left_lane_fit = np.polyfit(self.list_left_pts_y, self.list_left_pts_x, 2)
                arr_left_x = list_left_lane_fit[0] * arr_y ** 2 + list_left_lane_fit[1] * arr_y + list_left_lane_fit[2]
                arr_pts = np.array([np.transpose(np.vstack([arr_left_x, arr_y]))])
                cv2.polylines(img_trans, np.int_([arr_pts]), isClosed=False, color=(255, 0, 255), thickness=5)

                arr_x = np.add(arr_left_x, self.shift_pre)
                arr_pts = np.array([np.transpose(np.vstack([arr_x, arr_y]))])
                cv2.polylines(img_trans, np.int_([arr_pts]), isClosed=False, color=(255, 0, 0), thickness=5)

                self.cx_left_pre = int(arr_left_x[self.center_y])
                self.cx_right_pre = int(arr_left_x[self.center_y] + self.shift_pre * 2)
                self.gap_pre = self.shift_pre * 2
            except Exception as e:
                rospy.logerr("Fail.2 : " + e)
                return

        elif len(self.list_left_pts_x) <= 50 and len(self.list_right_pts_x) > 50:
            try:
                list_right_lane_fit = np.polyfit(self.list_right_pts_y, self.list_right_pts_x, 2)
                arr_right_x = list_right_lane_fit[0] * arr_y ** 2 + list_right_lane_fit[1] * arr_y + list_right_lane_fit[2]
                arr_pts = np.array([np.transpose(np.vstack([arr_right_x, arr_y]))])
                cv2.polylines(img_trans, np.int_([arr_pts]), isClosed=False, color=(255, 255, 0), thickness=5)

                arr_x = np.subtract(arr_right_x, self.shift_pre)
                arr_pts = np.array([np.transpose(np.vstack([arr_x, arr_y]))])
                cv2.polylines(img_trans, np.int_([arr_pts]), isClosed=False, color=(255, 0, 0), thickness=5)

                self.cx_right_pre = int(arr_right_x[self.center_y])
                self.cx_left_pre = int(arr_right_x[self.center_y] - self.shift_pre * 2)
                self.gap_pre = self.shift_pre * 2
            except Exception as e:
                rospy.logerr("Fail.3 : " + e)
                return

        else:
            rospy.logerr("Lane not found")
            cv2.imshow('img', img_ori)
            cv2.imshow('trans', img_trans)
            cv2.imshow('threshold', img_threshold)
            cv2.waitKey(1)
            return

        self.cx_pre = arr_x[self.center_y]
        err = arr_x[self.center_y] - self.center_x
        self.error_pub.publish(err)
        rospy.loginfo("Error : " + str(err))

        cv2.circle(img_trans, (self.center_x, self.center_y), 8, (255, 255, 0), 2)
        cv2.circle(img_trans, (int(arr_x[self.center_y]), self.center_y), 8, (255, 0, 0), 2)

        # Test Code
        cv2.imshow('img', img_ori)
        cv2.imshow('trans', img_trans)
        cv2.imshow('threshold', img_threshold)
        cv2.waitKey(1)

    @staticmethod
    def main():
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node("LaneProcessing_Node")
    node = LaneProcessServer()
    node.main()
