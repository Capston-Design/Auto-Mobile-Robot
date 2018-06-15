#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Control_Node.msg import Mission
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist
from parking_mission import ParkingMission
from tunnel_mission import TunnelMission
from traffic_mission import TrafficMission
from crossbar_mission import CrossbarMission
import rospy


class MissionNode:
    def __init__(self):
        # Cmd_val 관련 변수
        self.twist = Twist()

        # PID 제어 관련 변수
        self.kp = rospy.get_param("mission/lane/kp")
        self.ki = rospy.get_param("mission/lane/ki")
        self.kd = rospy.get_param("mission/lane/kd")
        self.dt = rospy.get_param("mission/lane/dt")
        self.max_vel = rospy.get_param("mission/lane/max_vel")
        self.last_err = 0
        self.sum_err = 0

        self.pub_value_lane = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.pub_value_stop = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.sub_error_lane = rospy.Subscriber('/error/controller/lane', Float32, self.cb_error_receive)
        self.sub_flag_mission = rospy.Subscriber('/flag/controller/mission', Mission, self.cb_bool_receive)

        # 갑자기 종료된 경우
        self.pub_value_stop.publish(rospy.on_shutdown(self.fn_on_shutdown))

    # 갑자기 종료된 경우 처리하는 메소드
    def fn_on_shutdown(self):
        rospy.loginfo("Shutting down. cmd_vel will be 0")
        self.twist = Twist()
        self.twist.linear.x = 0
        self.twist.angular.z = 0
        self.pub_value_stop.publish(self.twist)
        return self.twist

    def cb_error_receive(self, msg):
        err = msg.data
        ang_p = self.kp * err
        ang_i = self.ki * self.sum_err
        ang_d = self.kd * (err - self.last_err) / self.dt

        self.sum_err += err * self.dt
        self.last_err = err

        self.twist.linear.x = self.max_vel * ((1 - abs(err) / 384) ** 2)
        self.twist.angular.z = -float(ang_p + ang_i + ang_d)

        self.pub_value_lane.publish(self.twist)

    @staticmethod
    def cb_bool_receive(msg):
        if msg.traffic is True:
            if msg.crossbar or msg.parking or msg.tunnel is True:
                pass
            trm = TrafficMission()
        elif msg.crossbar is True:
            if msg.traffic or msg.parking or msg.tunnel is True:
                pass
            cm = CrossbarMission()
        elif msg.parking is True:
            if msg.traffic or msg.crossbar or msg.tunnel is True:
                pass
            pm = ParkingMission()
        elif msg.tunnel is True:
            if msg.traffic or msg.crossbar or msg.parking is True:
                pass
            tum = TunnelMission()

    @staticmethod
    def main():
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('Mission_Node')
    node = MissionNode()
    node.main()
