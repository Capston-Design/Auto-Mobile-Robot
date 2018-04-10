#!/usr/bin/env python
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
import os
import rospy
import cv2


FILE_COUNT = 0


def test_callback(msg):
    print("[INFO]Received an image!")

    global FILE_COUNT
    try:
        cvb = CvBridge()
        cv2_img = cvb.imgmsg_to_cv2(msg, "bgr8")
        cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
    except CvBridgeError, e:
        print(e)
    else:
        if FILE_COUNT % 5 == 0:
            print("[INFO]Saving an image!")
            count = len(os.walk('/home/seopaul/Capston-Design/Auto-Mobile-Robot/src/stack_image_node/data').next()[2])
            cv2.imwrite('../data/sample{}.png'.format(count + 1), cv2_img)

        FILE_COUNT += 1


def image_callback(msg):
    print("[INFO]Received an image!")
    try:
        cvb = CvBridge()
        cv2_img = cvb.imgmsg_to_cv2(msg, "bgr8")
        cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
    except CvBridgeError, e:
        print(e)
    else:
        global cnt
        if cnt % 5 == 0:
            print("[INFO]Saving an image!")

            f = open('../data/count.txt', 'r')
            count = f.readline()
            f.close()

            cv2.imwrite('../data/sample{}.png'.format(count), cv2_img)

            f = open('../data/count.txt', 'w')
            f.write(str(int(count) + 1))
            f.close()
        cnt += 1


def main():
    rospy.init_node('Camera_Image_Saver')
    rospy.Subscriber('image_raw', Image, test_callback, queue_size=5)
    rospy.spin()


if __name__ == '__main__':
    main()