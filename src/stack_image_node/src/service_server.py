#!/usr/bin/env python
import rospy
import os
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from stack_image_node.srv import *


def image_callback(msg):
    try:
        cvb = CvBridge()
        cv2_img = cvb.imgmsg_to_cv2(msg, "bgr8")
        cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
    except CvBridgeError, e:
        print(e)
    else:
        print("[INFO]Saving...")
        count = len(os.walk(PATH).next()[2])
        cv2.imwrite(PATH + '/sample{}.png'.format(count + 1), cv2_img)
        SUB.unregister()
        print("[INFO]Saving success!\n")


def image_request(request):
    print("[INFO]Request message come!")
    global PATH
    global SUB

    if request.flag_message == 'on':
        print("[INFO]Saving Mode!")
        SUB = rospy.Subscriber('image_raw', Image, image_callback)
        return SaveResponse(True)
    elif request.flag_message == 'off':
        print("[INFO]Non-Saving Mode!\n")
        return SaveResponse(True)
    else:
        print("[WARNING]Wrong message!\n")
        return SaveResponse(False)


def main():
    rospy.init_node('image_server')
    rospy.Service('image_request', Save, image_request)
    rospy.spin()

PATH = '/home/seopaul/Capston-Design/Auto-Mobile-Robot/src/stack_image_node/data'
SUB = None
main()
