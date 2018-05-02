#!/usr/bin/env python
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from ImageCollecting_Node.msg import ROI
import os
import rospy
import cv2


class ImageCollector:
    def __init__(self):
        self.sub_image_raw = rospy.Subscriber('image_raw', Image, self.cb_image_receive, queue_size=1)
        self.pub_image_roi = rospy.Publisher('image_roi', ROI, queue_size=1)
        self.cvb = CvBridge()
        self.roi_msg = ROI()

        self.path = '/home/seopaul/Capston-Design/Auto-Mobile-Robot/src/ImageCollecting_Node/data'
        self.save_flag = False
        self.file_count = 0

    def roi_crop(self, image, height, width):
        crop_image = image[height[0]:height[1], width[0]:width[1]]
        return crop_image

    def cb_image_save(self, img_list):
        count = (len(os.walk(self.path + '/road').next()[2]), len(os.walk(self.path + '/sign').next()[2]))
        cv2.imwrite(self.path + '/road/road{}.png'.format(count[0] + 1), img_list[0])
        cv2.imwrite(self.path + '/sign/sign{}.png'.format(count[1] + 1), img_list[1])
        rospy.loginfo("Save Complete!")

    def cb_image_receive(self, msg):
        try:
            cv2_img = self.cvb.imgmsg_to_cv2(msg, "bgr8")
        except CvBridgeError, e:
            print(e)
        else:
            height, width, __ = cv2_img.shape
            road = self.roi_crop(cv2_img, (height - 200, height - 100), (0, width))
            sign = self.roi_crop(cv2_img, (height - 400, height - 200), (0, width))
            img_list = [road, sign]

            if self.save_flag is True:
                if self.file_count % 100 == 0:
                    self.cb_image_save(img_list)
                    self.file_count = 0
                self.file_count += 1
            self.pb_image(img_list)

    def pb_image(self, img_list):
        for i in range(2):
            img_list[i] = self.cvb.cv2_to_imgmsg(img_list[i], encoding="bgr8")
        self.roi_msg.road_image = img_list[0]
        self.roi_msg.sign_image = img_list[1]
        self.pub_image_roi.publish(self.roi_msg)

    def main(self):
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('ImageCollecting_Node')
    node = ImageCollector()
    node.main()
