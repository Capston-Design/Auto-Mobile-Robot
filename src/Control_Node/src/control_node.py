#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ImageCollecting_Node.msg import ROI
from Control_Node.msg import Mission
from std_msgs.msg import Float32, String
from sensor_msgs.msg import Image
import rospy
import time


class ControlNode:
    def __init__(self):
        # Publish 시간을 통제하는 변수
        self.time_lane_pre = time.time()
        self.time_sign_pre = time.time()

        self.pub_img_lane = rospy.Publisher('/image/controller/lane', Image, queue_size=1)
        self.pub_img_sign = rospy.Publisher('/image/controller/sign', Image, queue_size=1)
        self.pub_error_lane = rospy.Publisher('/error/controller/lane', Float32, queue_size=1)
        self.pub_flag_mission = rospy.Publisher('/flag/controller/mission', Mission, queue_size=1)

        self.sub_img_roi = rospy.Subscriber('/image/image_collector/roi', ROI, self.cb_image_receive, queue_size=1)
        self.sub_error_lane = rospy.Subscriber('/error/lane_processor/lane', Float32, self.cb_error_receive, queue_size=1)
        self.sub_flag_sign = rospy.Subscriber('/flag/sign_processor/sign', String, self.cb_string_receive, queue_size=1)

    def cb_image_receive(self, msg):
        time_now = time.time()
        # Publish 시간을 통제하는 코드(10Hz 마다 Publish)
        if (time_now - self.time_lane_pre) > 0.1:
            self.pub_img_lane.publish(msg.road_image)
            self.time_lane_pre = time_now

        # Publish 시간을 통제하는 코드(10Hz 마다 Publish)
        if (time_now - self.time_sign_pre) > 0.1:
            self.pub_img_sign.publish(msg.sign_image)
            self.time_sign_pre = time_now

    def cb_error_receive(self, msg):
        self.pub_error_lane.publish(msg)

    def cb_string_receive(self, msg):
        if msg == 'traffic':
            print(1)
        elif msg == 'parking':
            print(2)
        elif msg == 'crossbar':
            print(3)
        elif msg == 'tunnel':
            print(4)

    @staticmethod
    def main():
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('Control_Node')
    node = ControlNode()
    node.main()


