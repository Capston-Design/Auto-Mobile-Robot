#!/usr/bin/env python
# -*-coding:utf-8-*-
import numpy as np
import cv2


class ImageProcessor:
    def __init__(self):
        self.height, self.width = 0, 0
        self.ratio_w, self.ratio_h = 300, 350
        self.list_pos_pre, self.list_pos = [], []

    def perspective_transform(self, image):
        mask_line = self.hsv_filter(image)
        img_line = cv2.bitwise_and(image, image, mask=mask_line)

        self.height, self.width = img_line.shape[:2]

        val_left_w0 = 0
        val_left_h0 = int(self.height / 4)
        img_left = img_line[val_left_h0: val_left_h0 + (int(self.height/2)),
                            val_left_w0: val_left_w0 + (int(self.width / 2))]

        val_right_w0 = int(self.width / 2)
        val_right_h0 = int(self.height / 4)
        img_right = img_line[val_right_h0: val_right_h0 + (int(self.height / 2)),
                             val_right_w0: val_right_w0 + (int(self.width/2))]

        img_left_edges = cv2.Canny(img_left, 80, 180)
        img_right_edges = cv2.Canny(img_right, 80, 180)

        list_hough_left = cv2.HoughLines(img_left_edges, 1, np.pi/180, 30)
        list_hough_right = cv2.HoughLines(img_right_edges, 1, np.pi/180, 30)

        list_left_x0 = [rho * np.cos(theta) for [[rho, theta]] in list_hough_left[:2]]
        idx_left = list_left_x0.index(max(list_left_x0))
        [[rho, theta]] = list_hough_left[idx_left]
        line_left = self.hough_pos(rho, theta, val_left_w0, val_left_h0, self.height)

        list_right_x0 = [rho * np.cos(theta) for [[rho, theta]] in list_hough_right[:2]]
        idx_right = list_right_x0.index(min(list_right_x0))
        [[rho, theta]] = list_hough_right[idx_right]
        line_right = self.hough_pos(rho, theta, val_right_w0, val_right_h0, self.height)

        x_mid = (line_left[0][0] + line_right[0][0] + line_left[1][0] + line_right[1][0]) // 4 * 1.2
        x_width = ((line_left[1][1] + line_right[1][1]) - (line_left[0][1] + line_right[0][1])) * self.ratio_w // (4 * self.ratio_h) * 2

        pos1_pre = [line_left[0][0], line_left[0][1]]
        pos1 = [x_mid - x_width, line_left[0][1] * 2]
        pos2_pre = [line_left[1][0], line_left[1][1]]
        pos2 = [x_mid - x_width, line_left[1][1] * 2]
        pos3_pre = [line_right[0][0], line_right[0][1]]
        pos3 = [x_mid + x_width, line_right[0][1] * 2]
        pos4_pre = [line_right[1][0], line_right[1][1]]
        pos4 = [x_mid + x_width, line_right[1][1] * 2]

        self.list_pos_pre = [pos1_pre, pos2_pre, pos3_pre, pos4_pre]
        self.list_pos = [pos1, pos2, pos3, pos4]
        return self.list_pos_pre, self.list_pos

    @staticmethod
    def hough_pos(rho, theta, w0, h0, height):
        c_theta = np.cos(theta)
        s_theta = np.sin(theta)
        x0 = w0 + c_theta*rho
        y0 = h0 + s_theta*rho
        r1 = y0 // c_theta
        r2 = (height - y0) // c_theta
        upper_x = int(x0 - r1 * (-s_theta))
        upper_y = int(y0 - r1 * c_theta)
        lower_x = int(x0 + r2 * (-s_theta))
        lower_y = int(y0 + r2 * c_theta)
        return [[upper_x, upper_y], [lower_x, lower_y]]

    @staticmethod
    def hsv_filter(image):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # HSV_White color  [0,0,200] [255,255,255]
        # HSV_White color  [70,10,130] [180,110,255]
        lower_white = np.array([0, 0, 230], np.uint8)
        upper_white = np.array([255, 255, 255], np.uint8)
        mask_w = cv2.inRange(hsv, lower_white, upper_white)

        # HSV_Yellow color [20,100,100] [30,255,255]
        lower_yellow = np.array([20, 100, 100], np.uint8)
        upper_yellow = np.array([30, 255, 255], np.uint8)
        mask_y = cv2.inRange(hsv, lower_yellow, upper_yellow)

        mask_line = cv2.add(mask_w, mask_y)
        return mask_line
