#!/usr/bin/env python
# -*-coding:utf-8-*-
from lanedetector import LaneDetector
from std_msgs.msg import Float32
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import rospy
import time


class LaneProcessServer:
    def __init__(self):
        # FPS 연산에 사용하는 변수
        self.prev_time = 0

        # 외부에서 이미지를 받아오는 설정
        self.cvb = CvBridge()
        self.lane = LaneDetector((60, 320))

        self.image_sub = rospy.Subscriber('/image/controller/lane', Image, self.image_callback, queue_size=1)
        self.error_pub = rospy.Publisher('/error/lane_processor/lane', Float32, queue_size=1)
        self.image_pub = rospy.Publisher('/image/lane_processor/lane', Image, queue_size=1)
        self.pers_pub = rospy.Publisher('/image/lane_processor/perspective', Image, queue_size=1)

    def image_callback(self, msg):
        img_ori = self.cvb.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        # FPS 를 구하는 과정
        cur_time = time.time()
        f = 1 / (cur_time - self.prev_time)
        self.prev_time = cur_time

        error = self.lane(img_ori, f)

        msg = self.cvb.cv2_to_imgmsg(self.lane.process[6][1], encoding='bgr8')
        pers = self.cvb.cv2_to_imgmsg(self.lane.process[5][1], encoding='mono8')
        self.error_pub.publish(float(error))
        self.image_pub.publish(msg)
        self.pers_pub.publish(pers)
        del self.lane.process[:]

    @staticmethod
    def main():
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node("LaneProcessing_Node")
    node = LaneProcessServer()
    node.main()

