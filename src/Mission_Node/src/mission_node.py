#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Control_Node.msg import Mission
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist
from lane_mission import LaneMission
from parking_mission import ParkingMission
from tunnel_mission import TunnelMission
from traffic_mission import TrafficMission
from crossbar_mission import CrossbarMission
import rospy


class MissionNode:
    def __init__(self):
        # TODO : 미션의 번호가 날아오면 해당미션을 실행
        self.pub_value_lane = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.sub_error_lane = rospy.Subscriber('/error/controller/lane', Float32, self.cb_error_receive)
        self.sub_bool_mission = rospy.Subscriber('/bool/controller/mission', Mission, self.cb_bool_receive)

    def cb_error_receive(self, msg):
        lm = LaneMission(msg)
        twist_msg = lm.fn_pid_control(msg.data)
        self.pub_value_lane.publish(twist_msg)

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
