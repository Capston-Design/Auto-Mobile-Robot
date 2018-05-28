#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ImageProcessing_Node.msg import DetectSignGoal, DetectSignResult, DetectSignFeedback, DetectSignAction
from ImageCollecting_Node.msg import ROI
from Control_Node.msg import Mission
from std_msgs.msg import Float32
from sensor_msgs.msg import Image
import actionlib
import rospy


class ControlNode:
    def __init__(self):
        self.pub_img_lane = rospy.Publisher('/image/controller/lane', Image, queue_size=1)
        self.pub_error_lane = rospy.Publisher('/error/controller/lane', Float32, queue_size=1)
        self.pub_bool_mission = rospy.Publisher('/bool/controller/mission', Mission, queue_size=1)

        self.act_img_sign = actionlib.SimpleActionClient('/image/controller/sign', DetectSignAction)
        self.sub_img_roi = rospy.Subscriber('/image/image_collector/roi', ROI, self.cb_image_receive)
        self.sub_error_lane = rospy.Subscriber('/error/image_processor/lane', Float32, self.cb_error_receive)

    def cb_image_receive(self, msg):
        self.fn_publish_lane(msg=msg.road_image)
        self.fn_action_sign(msg=msg.sign_image)

    def cb_feedback(self, feedback):
        rospy.loginfo("Status : " + feedback.status + ", Number : " + str(feedback.detect_num))

        msg = Mission()
        if feedback.detect_num == 1:
            msg.traffic = True
            msg.crossbar = False
            msg.parking = False
            msg.tunnel = False
        elif feedback.detect_num == 2:
            msg.traffic = False
            msg.crossbar = True
            msg.parking = False
            msg.tunnel = False
        elif feedback.detect_num == 3:
            msg.traffic = False
            msg.crossbar = False
            msg.parking = True
            msg.tunnel = False
        elif feedback.detect_num == 4:
            msg.traffic = False
            msg.crossbar = False
            msg.parking = False
            msg.tunnel = True
        else:
            return
        self.pub_bool_mission.publish(msg)

    def cb_error_receive(self, msg):
        rospy.loginfo("ERROR : " + str(msg.data))
        self.pub_error_lane.publish(msg)

    # TODO: 수정이 필요
    def fn_action_sign(self, msg):
        self.act_img_sign.wait_for_server()

        goal = DetectSignGoal()
        goal.sign_img = msg

        self.act_img_sign.send_goal(goal, feedback_cb=self.cb_feedback)
        print()
        self.act_img_sign.wait_for_result()
        rospy.loginfo("Result : " + self.act_img_sign.get_result().result)

    def fn_publish_lane(self, msg):
        self.pub_img_lane.publish(msg)

    @staticmethod
    def main():
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('Control_Node')
    node = ControlNode()
    node.main()


