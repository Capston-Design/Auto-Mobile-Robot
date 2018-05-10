#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy


class CrossbarMission:
    def __init__(self):
        print("test")

    @staticmethod
    def main():
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('CrossbarMission')
    node = CrossbarMission()
    node.main()
