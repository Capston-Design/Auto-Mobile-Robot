#!/usr/bin/env python
from find_object_2d.msg import ObjectsStamped
import rospy
import math
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal


class imageprocess:
    def __init__(self):
        self.sub_objectsStamped = rospy.Subscriber('objectsStamped',ObjectsStamped, self.find_callback, queue_size=1)

        self.test_flag = False
        self.Point_x = 0.0
        self.Point_y = 0.0
        self.Angle = math.radians(0)
        self.GoalPoint = [self.Point_x, self.Point_y, 0.0, 0.0, 0.0, math.sin(self.Angle / 2), math.cos(self.Angle / 2)]
        self.find_object_number = 0.0

    def move_goal(self, pose):
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

    def find_callback(self, msg):
        try:
            self.find_object_number = msg.objects.data[0]
            self.test_flag = True
	     

        except:
            pass

        else:
            if(self.find_object_number == 39.0):
                print('[Detect] Professor_Lee_Gwihyeong : 916') 
                self.Point_x = 2.70
                self.Point_y = -0.158
          
                self.GoalPoint = [self.Point_x, self.Point_y, 0.0, 0.0, 0.0, 0.239, 0.971] 

            if(self.find_object_number == 40.0):
                print('[Detect] ADBL_center : 901') 
                self.Point_x = 4.960
                self.Point_y = -5.579
                self.Angle = math.radians(0)
                self.GoalPoint = [self.Point_x, self.Point_y, 0.0, 0.0, 0.0,0.956, -0.262]
            if self.test_flag is True:
                self.sub_objectsStamped.unregister()
                client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
                client.wait_for_server()
                goal = self.move_goal(self.GoalPoint)
                client.send_goal(goal)
                client.wait_for_result()
                self.test_flag = False
                self.sub_objectsStamped = rospy.Subscriber('objectsStamped', ObjectsStamped, self.find_callback,
                                                           queue_size=1)

    def main(self):
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('Find_Object_Node')
    node = imageprocess()
    node.main()









