#!/usr/bin/env python
# -*- coding: utf-8 -*-
from geometry_msgs.msg import Twist
import rospy

class LaneMission:
    def __init__(self, msg):
        self.twist = Twist()

        self.kp = rospy.get_param("mission/lane/kp")
        self.ki = rospy.get_param("mission/lane/ki")
        self.kd = rospy.get_param("mission/lane/kd")
        self.dt = rospy.get_param("mission/lane/dt")
        self.max_vel = rospy.get_param("mission/lane/max_vel")

        self.last_err = 0
        self.sum_err = 0

    def fn_pid_control(self, err):
        ang_p = self.kp * err
        ang_i = self.ki * self.sum_err
        ang_d = self.kd * (err - self.last_err) / self.dt

        self.sum_err += err * self.dt
        self.last_err = err
        self.twist.linear.x = self.max_vel * ((1 - abs(err) / 384) ** 2)
        self.twist.angular.z = -float(ang_p + ang_i + ang_d)
        return self.twist

if __name__ == '__main__':
    lm = LaneMission()
