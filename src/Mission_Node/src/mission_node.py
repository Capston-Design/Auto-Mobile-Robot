#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy


class MissionNode:
    def __init__(self):
        print("test")

    @staticmethod
    def main():
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('Mission_Node')
    node = MissionNode()
    node.main()
