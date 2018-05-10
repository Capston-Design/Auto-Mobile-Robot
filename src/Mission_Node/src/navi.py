#!/usr/bin/env python

import rospy , math
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from find_object_2d.msg import ObjectsStamped  


#find_object_number = 0.0
#Point_x,Point_y,Angle = raw_input("Point_x , Point_y , Angle :").split(',')
#Point_x,Point_y,Angle = [float(Point_x),float(Point_y),float(Angle)]

def find_callback(msg):
    try:
        find_object_number = msg.objects.data[0]
        print(find_object_number)
        
    except:
        #print(find_object_number)
	 pass
    else:
        sub.unregister()
        if (find_object_number == 34.0):
            Point_x=0.0
            Point_y=0.0

            Angle = math.radians(0) #input degrees
            GoalPoint = [ Point_x, Point_y, 0.0 , 0.0, 0.0, math.sin(Angle/2), math.cos(Angle/2) ]

            #rospy.init_node("MoveTBtoGoal")
            client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
            client.wait_for_server()

            goal = move_goal(GoalPoint)
            client.send_goal(goal)
   
            client.wait_for_result()


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


rospy.init_node('find_ob')

global sub
sub = rospy.Subscriber('objectsStamped',ObjectsStamped, find_callback,queue_size=1)
rospy.spin()


