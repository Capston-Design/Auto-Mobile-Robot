#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy


class TunnelMission:
    def __init__(self):
        print("test")

    @staticmethod
    def main():
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('TunnelMission')
    node = TunnelMission()
    node.main()
