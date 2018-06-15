#!/usr/bin/env python
# -*- coding: utf-8 -*-
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from ImageCollecting_Node.msg import ROI
import time
import os
import rospy
import cv2


class ImageCollectingNode:
    def __init__(self):
        # Deep Learning 데이터 수집에 필요한 이미지를 저장하는 경로
        self.__path = os.path.realpath(os.path.dirname(__file__))\
            .replace('ImageCollecting_Node/src', 'ImageCollecting_Node/data')

        # Flag 가 True 일 때만 이미지 저장기능 활성화
        self.__save_flag = False
        if self.__save_flag is True:
            self.time_save_pre = time.time()

        # Uvc_Camera 에서 받아온 이미지를 변환할 때 사용하는 객체
        self.cvb = CvBridge()

        # 사용자 지정 메시지 객체
        self.msg_roi = ROI()

        # Topic 관련 객체
        self.pub_img_roi = rospy.Publisher('/image/image_collector/roi', ROI, queue_size=1)
        self.sub_img_raw = rospy.Subscriber('/image_raw', Image, self.cb_image_receive, queue_size=1)

    def cb_image_receive(self, msg):
        # Uvc_Camera 에서 받아온 이미지를 cv2 로 변환
        cv2_img = self.cvb.imgmsg_to_cv2(msg, "bgr8")

        # ROI 영역에 따라서 자르는 과정
        height, width = cv2_img.shape[:2]
        road = cv2_img[height//2 + 60:height, 0:width]
        sign = cv2_img[0:height//2 + 60, 0:width]
        img_list = [road, sign]

        # Flag 에 따라서 저장할 수 있는 기능
        if self.__save_flag is True:
            time_now = time.time()
            if (time_now - self.time_save_pre) > 1:
                count = (len(os.walk(self.__path + '/road').next()[2]), len(os.walk(self.__path + '/sign').next()[2]))
                cv2.imwrite(self.__path + '/road/road{}.png'.format(count[0] + 1), img_list[0])
                cv2.imwrite(self.__path + '/sign/sign{}.png'.format(count[1] + 1), img_list[1])
                rospy.loginfo("Save Complete!")
                self.time_save_pre = time_now

        # ROI.msg 형태로 메시지를 작성하고 Publish
        for i in range(2):
            img_list[i] = self.cvb.cv2_to_imgmsg(img_list[i], encoding="bgr8")
        self.msg_roi.road_image = img_list[0]
        self.msg_roi.sign_image = img_list[1]
        self.pub_img_roi.publish(self.msg_roi)

    @staticmethod
    def main():
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('ImageCollecting_Node')
    node = ImageCollectingNode()
    node.main()
