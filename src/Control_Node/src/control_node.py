#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ImageCollecting_Node.msg import ROI
from cv_bridge import CvBridge, CvBridgeError
import rospy
import cv2
import subprocess

class Controller:
    def __init__(self):
        self.sub_image_roi = rospy.Subscriber('image_roi', ROI, self.cb_image_receive)
        self.cvb = CvBridge()
        self.flag = True

    def cb_image_receive(self, msg):
        try:
            cv2_img_road = self.cvb.imgmsg_to_cv2(msg.road_image, "passthrough")
            cv2_img_sign = self.cvb.imgmsg_to_cv2(msg.sign_image, "passthrough")
            if self.flag is True:
                cv2.imshow("cv2_img_road", cv2_img_road)
                cv2.imshow("cv2_img_sign", cv2_img_sign)
                self.flag = False
            cv2.waitKey(0)
        except CvBridgeError, e:
            print(e)

    def main(self):
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('Control_Node')
    node = Controller()
    node.main()


