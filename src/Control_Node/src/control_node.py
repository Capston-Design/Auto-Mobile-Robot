#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ImageProcessing_Node.msg import DetectSignGoal, DetectSignResult, DetectSignFeedback, DetectSignAction
from ImageCollecting_Node.msg import ROI
from std_msgs.msg import Float32
from sensor_msgs.msg import Image
import actionlib
import rospy


class Controller:
    def __init__(self):
        self.pub_img_lane = rospy.Publisher('/image/controller/lane', Image, queue_size=1)
        self.pub_error_lane = rospy.Publisher('/error/controller/lane', Float32, queue_size=1)
        self.act_img_sign = actionlib.SimpleActionClient('/image/controller/sign', DetectSignAction)
        self.sub_img_roi = rospy.Subscriber('/image/image_collector/roi', ROI, self.cb_image_receive)
        self.sub_error_lane = rospy.Subscriber('/error/image_processor/lane', Float32, self.cb_error_receive)

    def cb_image_receive(self, msg):
        self.fn_publish_lane(msg=msg.road_image)
        self.fn_action_sign(msg=msg.sign_image)

    @staticmethod
    def cb_feedback(feedback):
        rospy.loginfo("Status : " + feedback.status + ", Number : " + str(feedback.detect_num))

    def cb_error_receive(self, msg):
        self.pub_error_lane.publish(msg)

    def fn_publish_lane(self, msg):
        self.pub_img_lane.publish(msg.road_image)

    # TODO: 수정이 필요
    def fn_action_sign(self, msg):
        self.act_img_sign.wait_for_server()

        goal = DetectSignGoal()
        goal.sign_img = msg

        self.act_img_sign.send_goal(goal, feedback_cb=self.cb_feedback)
        print()
        self.act_img_sign.wait_for_result()
        rospy.loginfo("Result : " + self.act_img_sign.get_result().result)

    @staticmethod
    def main():
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('Control_Node')
    node = Controller()
    node.main()


