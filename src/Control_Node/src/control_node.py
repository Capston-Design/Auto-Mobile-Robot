#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ImageCollecting_Node.msg import ROI
from Control_Node.msg import Mission
from std_msgs.msg import Float32
from sensor_msgs.msg import Image
import rospy


class ControlNode:
    def __init__(self):
        self.pub_img_lane = rospy.Publisher('/image/controller/lane', Image, queue_size=1)
        self.pub_img_sign = rospy.Publisher('/image/controller/sign', Image, queue_size=1)
        self.pub_error_lane = rospy.Publisher('/error/controller/lane', Float32, queue_size=1)
        self.pub_bool_mission = rospy.Publisher('/bool/controller/mission', Mission, queue_size=1)

        self.sub_img_roi = rospy.Subscriber('/image/image_collector/roi', ROI, self.cb_image_receive, queue_size=1)
        self.sub_error_lane = rospy.Subscriber('/error/image_processor/lane', Float32, self.cb_error_receive, queue_size=1)

    def cb_image_receive(self, msg):
        # TODO: Publish 시간을 통제하는 코드(20Hz 마다 Publish)
        self.pub_img_lane.publish(msg.road_image)

        # TODO: Publish 시간을 통제하는 코드(10Hz 마다 Publish)
        self.pub_img_sign.publish(msg.sign_image)

    def cb_error_receive(self, msg):
        self.pub_error_lane.publish(msg)

    @staticmethod
    def main():
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('Control_Node')
    node = ControlNode()
    node.main()


