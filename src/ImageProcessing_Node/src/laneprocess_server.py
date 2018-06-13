#!/usr/bin/env python
# -*-coding:utf-8-*-
from lanedetector import LaneDetector
from std_msgs.msg import Float32
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy as np
import cv2
import rospy
import time


class LaneProcessServer:
    def __init__(self):
        # Test
        self.prev_time = 0

        self.cvb = CvBridge()
        self.lane = LaneDetector((40, 320))

        self.image_sub = rospy.Subscriber('/image/controller/lane', Image, self.image_callback, queue_size=1)
        self.error_pub = rospy.Publisher('/error/image_processor/lane', Float32, queue_size=1)

    def image_callback(self, msg):
        img_ori = self.cvb.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        # FPS 를 구하는 과정
        cur_time = time.time()
        f = 1 / (cur_time - self.prev_time)
        self.prev_time = cur_time

        error = self.lane(img_ori, f)
        for process in self.lane.process:
            cv2.imshow(process[0], process[1])
        del self.lane.process[:]
        cv2.waitKey(1)

        self.error_pub.publish(float(error))

    @staticmethod
    def main():
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node("LaneProcessing_Node")
    node = LaneProcessServer()
    node.main()

