#!/usr/bin/env python
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from ImageCollecting_Node.msg import ROI
import os
import rospy
import cv2


class ImageCollectingNode:
    def __init__(self):
        self.path = self.fn_load()

        self.save_flag = False
        self.file_count = 0

        self.cvb = CvBridge()
        self.msg_roi = ROI()

        self.pub_img_roi = rospy.Publisher('/image/image_collector/roi', ROI, queue_size=1)
        self.sub_img_raw = rospy.Subscriber('/image_raw', Image, self.cb_image_receive, queue_size=1)

    @staticmethod
    def fn_load():
        dir_path = os.path.realpath(os.path.dirname(__file__))
        dir_path = dir_path.replace('ImageCollecting_Node/src', 'ImageCollecting_Node/data')
        return dir_path

    @staticmethod
    def roi_crop(image, height, width):
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
                if self.file_count % 30 == 0:
                    self.cb_image_save(img_list)
                    self.file_count = 0
                self.file_count += 1
            self.fn_publish_roi(img_list)

    def fn_publish_roi(self, img_list):
        for i in range(2):
            img_list[i] = self.cvb.cv2_to_imgmsg(img_list[i], encoding="bgr8")
        self.msg_roi.road_image = img_list[0]
        self.msg_roi.sign_image = img_list[1]
        self.pub_img_roi.publish(self.msg_roi)

    @staticmethod
    def main():
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('ImageCollecting_Node')
    node = ImageCollectingNode()
    node.main()
