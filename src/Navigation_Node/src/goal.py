#!/usr/bin/env python

import rospy , math
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import PoseWithCovarianceStamped


Point_x=0.0
Point_y=-0.0
Angle = math.radians(0) #input degrees

#Point_x,Point_y,Angle = raw_input("Point_x , Point_y , Angle :").split(',')
#Point_x,Point_y,Angle = [float(Point_x),float(Point_y),float(Angle)]

GoalPoint = [ Point_x, Point_y, 0.0 , 0.0, 0.0, math.sin(Angle/2), math.cos(Angle/2) ]

def move_goal(pose):
    navi_goal = MoveBaseGoal()
    navi_goal.target_pose.header.frame_id = 'map'
    navi_goal.target_pose.pose.position.x = pose[0]
    navi_goal.target_pose.pose.position.y = pose[1]
    navi_goal.target_pose.pose.position.z = pose[2]
    navi_goal.target_pose.pose.orientation.x = pose[3]
    navi_goal.target_pose.pose.orientation.y = pose[4]
    navi_goal.target_pose.pose.orientation.z = pose[5]
    navi_goal.target_pose.pose.orientation.w = pose[6]

    return navi_goal


def initial_pose_pub():    	   
    pub = rospy.Publisher('initialpose',PoseWithCovarianceStamped, queue_size=1)
    initial_pose = PoseWithCovarianceStamped()
    initial_pose.header.frame_id = 'map'
    initial_pose.header.stamp = rospy.Time.now()
    initial_pose.pose.pose.position.x = 0.0
    initial_pose.pose.pose.position.y = 0.0
    initial_pose.pose.pose.position.z = 0.0
    initial_pose.pose.pose.orientation.x = 0.0
    initial_pose.pose.pose.orientation.y = 0.0
    initial_pose.pose.pose.orientation.z = 0.0
    initial_pose.pose.pose.orientation.w = 0.0
    initial_pose.pose.covariance = [0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.06853891945200942]
    #rospy.loginfo(initial_pose)
    pub.publish(initial_pose)
	    

if __name__ == '__main__':
    rospy.init_node("MovetoGoal")
    initial_pose_pub()
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()

    goal = move_goal(GoalPoint)
    client.send_goal(goal)

    client.wait_for_result()

