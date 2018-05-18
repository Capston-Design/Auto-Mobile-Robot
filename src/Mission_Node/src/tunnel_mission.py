#!/usr/bin/env python
# -*- coding: utf-8 -*-
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import rospy
import math
import actionlib


class TunnelMission:
    def __init__(self):
        self.run()

    def run(self):
        print("test")

if __name__ == '__main__':
    tum = TunnelMission()
