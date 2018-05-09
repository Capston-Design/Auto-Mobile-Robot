#!/usr/bin/env python
# -*-coding:utf-8-*-
from ImageProcessing_Node.msg import DetectLaneAction, DetectLaneGoal, DetectLaneResult, DetectLaneFeedback
import rospy


class LaneProcessServer:
    def __init__(self):
        print("test")

    @staticmethod
    def main():
        rospy.spin()


if __name__ == '__main__':
    rospy.init_node("LaneProcessing_Node")
    node = LaneProcessServer()
    node.main()
