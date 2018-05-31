#!/usr/bin/env python
# -*-coding:utf-8-*-
from cv_bridge import CvBridge
from std_msgs.msg import Float32
from sensor_msgs.msg import Image
import cv2
import numpy as np
import rospy


class LaneDetector:
    def __init__(self):
        # Perspective 변환에 필요한 초기좌표
        self.list_pos_ori = [[100, 0], [0, 192], [665, 0], [765, 192]]
        self.list_pos_trans = [[105, 0], [200, 400], [795, 0], [700, 400]]

        # Center 에서 가장 가까운 점들의 정보리스트
        self.distance_info_left, self.distance_info_right, self.left_min, self.right_min = [], [], [], []
        self.noise_filter = 100

        self.bridge = CvBridge()

        self.image_sub = rospy.Subscriber('/image/controller/lane', Image, self._cb_image)
        self.image_pub = rospy.Publisher('/image/image_processor/lane', Image, queue_size=1)

        self.canny_pub = rospy.Publisher('/image/image_processor/canny', Image, queue_size=1)
        self.dot_pub = rospy.Publisher('/image/image_processor/dot', Image, queue_size=1)
        # self.error_pub = rospy.Publisher('/error/image_processor/lane', Float32, queue_size=1)

    def _cb_image(self, msg):
        # 원본이미지 관련 변수
        self.ori_img = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        self.ori_height, self.ori_width = self.ori_img.shape[:2]

        self.run()

    def _set_center(self):
        center_img = np.zeros((self.p_height, self.p_width, 3), 'uint8')
        cv2.line(center_img, (self.p_width // 2, 0), (self.p_width // 2, self.p_height), (255, 0, 0), 3)
        return center_img

    def _set_line(self):
        line_img = np.zeros((self.p_height, self.p_width))
        offset = self.p_height // self.num_of_section
        pre_pos = 0
        for i in range(0, self.num_of_section):
            line_img = cv2.line(line_img, (0, pre_pos + offset), (self.p_width, pre_pos + offset), (255, 255, 255), 1)
            pre_pos += offset
        return line_img

    def _fn_init_setting(self):
        self.distance_info_left = []
        self.distance_info_right = []
        self.left_min = []
        self.right_min = []

    def _fn_common_dot(self, img):
        for h in range(0, self.p_height):
            for w in range(0, self.p_width):
                distance = self.p_width // 2 - w
                if self.line_img[h, w] != 0 and img[h, w] != 0:
                    if distance > self.noise_filter:
                        self.distance_info_left.append([h, w, abs(self.p_width // 2 - w)])
                        # img[h, w] = 255
                    elif distance < -self.noise_filter:
                        self.distance_info_right.append([h, w, abs(self.p_width // 2 - w)])
                        # img[h, w] = 255
                    else:
                        # img[h, w] = 0
                        pass
                else:
                    # img[h, w] = 0
                    pass
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

        # Dot 이미지 중에서 중앙선과 최소거리를 가지는 점의 정보만 리스트에 저장
        self._fn_min_distance(self.distance_info_left, self.left_min)
        self._fn_min_distance(self.distance_info_right, self.right_min)

        res = np.zeros((self.p_height, self.p_width, 3), 'uint8')
        for num in range(0, len(self.left_min)):
            # cv2.circle(res, (self.distance_info_min[num][0], self.distance_info_min[num][1]), 1, (0, 255, 0), -1)
            res[self.left_min[num][0]][self.left_min[num][1]] = 255
        for num in range(0, len(self.right_min)):
            # cv2.circle(res, (self.distance_info_min[num][0], self.distance_info_min[num][1]), 1, (0, 255, 0), -1)
            res[self.right_min[num][0]][self.right_min[num][1]] = 255

        return res

    def _fn_perspective(self, img, pos_ori, pos_trans):
        arr_pos_ori = np.float32(pos_ori)
        arr_pos_trans = np.float32(pos_trans)
        mat_perspective = cv2.getPerspectiveTransform(arr_pos_ori, arr_pos_trans)
        img_trans = cv2.warpPerspective(img, mat_perspective, (int(self.ori_width * 1.2), self.ori_height * 2))
        return img_trans

    @staticmethod
    def _fn_min_distance(info_list, result_list):
        pre_h = []
        distance = []
        for num in range(0, len(info_list)):
            if num == 0:
                pre_h = info_list[num]
                distance = pre_h
                continue

            if pre_h[0] == info_list[num][0]:
                if distance[2] > info_list[num][2]:
                    distance = info_list[num]
            else:
                result_list.append(distance)
                pre_h = info_list[num]
                distance = pre_h

    def run(self):
        gray = cv2.cvtColor(self.ori_img, cv2.COLOR_BGR2GRAY)
        __, threshold = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)
        canny = cv2.Canny(threshold, 150, 200, apertureSize=7)

        # Perspective 이미지 관련 변수
        self.p_img = self._fn_perspective(canny, self.list_pos_ori, self.list_pos_trans)
        self.p_height, self.p_width = self.p_img.shape[:2]

        # Center 이미지 관련 변수
        self.center_img = self._set_center()

        # Line 이미지 관련 변수
        self.num_of_section = 70
        self.line_img = self._set_line()
        dot = self._fn_common_dot(self.p_img)

        left_x, left_y = [], []
        for num in range(0, len(self.left_min)):
            left_x.append(self.left_min[num][0])
            left_y.append(self.left_min[num][1])

        right_x, right_y = [], []
        for num in range(0, len(self.right_min)):
            right_x.append(self.right_min[num][0])
            right_y.append(self.right_min[num][1])

        if len(left_x) > 5 and len(left_y) > 5:
            arr_y = np.linspace(0, self.p_height - 1, self.p_height)

            left = np.polyfit(left_x, left_y, 2)
            arr_left_x = left[0] * arr_y ** 2 + left[1] * arr_y + left[2]
            arr_pts = np.array([np.transpose(np.vstack([arr_left_x, arr_y]))])
            cv2.polylines(dot, np.int_([arr_pts]), isClosed=False, color=(255, 255, 0), thickness=1)

            right = np.polyfit(right_x, right_y, 2)
            arr_right_x = right[0] * arr_y ** 2 + right[1] * arr_y + right[2]
            arr_pts = np.array([np.transpose(np.vstack([arr_right_x, arr_y]))])
            cv2.polylines(dot, np.int_([arr_pts]), isClosed=False, color=(255, 255, 0), thickness=1)

            dot_center = cv2.add(self.center_img, dot)
            # result = cv2.add(self.p_img, dot_center)

            c = self.bridge.cv2_to_imgmsg(canny, encoding="mono8")
            self.canny_pub.publish(c)
            d = self.bridge.cv2_to_imgmsg(dot_center, encoding="bgr8")
            self.dot_pub.publish(d)

            # msg = self.bridge.cv2_to_imgmsg(result, encoding="bgr8")
            # self.image_pub.publish(msg)
        else:
            rospy.logerr("Line Error")

        self._fn_init_setting()

    @staticmethod
    def main():
        rospy.spin()


if __name__ == "__main__":
    rospy.init_node('"LaneTesting_Node"')
    node = LaneDetector()
    node.main()
