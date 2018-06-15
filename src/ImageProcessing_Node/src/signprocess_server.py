#!/usr/bin/env python
# -*-coding:utf-8-*-
from objectdetector import ObjectDetector
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
import rospy
import time
import cv2


class SignProcessServer:
    def __init__(self):
        # FPS 연산에 사용하는 변수
        self.prev_time = 0

        # 외부에서 이미지를 받아오는 설정
        self.cvb = CvBridge()
        self.object = ObjectDetector()

        self.image_sub = rospy.Subscriber('/image/controller/sign', Image, self.image_callback, queue_size=1)
        self.flag_pub = rospy.Publisher('/flag/sign_processor/sign', String, queue_size=1)
        self.image_pub = rospy.Publisher('/image/sign_processor/sign', Image, queue_size=1)

    def image_callback(self, msg):
        img_ori = self.cvb.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        # FPS 를 구하는 과정
        cur_time = time.time()
        f = 1 / (cur_time - self.prev_time)
        self.prev_time = cur_time

        result = self.object(img_ori, f)
        result[0] = self.cvb.cv2_to_imgmsg(result[0], encoding='bgr8')
        self.image_pub.publish(result[0])
        self.flag_pub.publish(result[1])

    @staticmethod
    def main():
        rospy.spin()


if __name__ == '__main__':
    rospy.init_node("SignProcessing_Node")
    node = SignProcessServer()
    node.main()

