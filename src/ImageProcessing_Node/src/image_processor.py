#!/usr/bin/env python
# -*-coding:utf-8-*-
import numpy as np
import cv2


class ImageProcessor:
    def __init__(self):
        pass

    @staticmethod
    def hsv_filter(image):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # HSV_White color  [0,0,200] [255,255,255]
        # HSV_White color  [70,10,130] [180,110,255]
        lower_white = np.array([0, 0, 2220], np.uint8)
        upper_white = np.array([255, 255, 255], np.uint8)
        mask_w = cv2.inRange(hsv, lower_white, upper_white)

        # HSV_Yellow color [20,100,100] [30,255,255]
        lower_yellow = np.array([15, 100, 100], np.uint8)
        upper_yellow = np.array([35, 255, 255], np.uint8)
        mask_y = cv2.inRange(hsv, lower_yellow, upper_yellow)

        mask_line = cv2.add(mask_w, mask_y)
        return mask_line

    @staticmethod
    def trans_perspective(image, pos_ori, pos_trans):
        val_ori_h, val_ori_w = image.shape[:2]
        arr_pos_ori = np.float32(pos_ori)
        arr_pos_trans = np.float32(pos_trans)
        mat_perspective = cv2.getPerspectiveTransform(arr_pos_ori, arr_pos_trans)
        img_trans = cv2.warpPerspective(image, mat_perspective, (int(val_ori_w * 1.2), val_ori_h * 2))
        return img_trans

    @staticmethod
    def end_in_search(image, per_low, per_high):
        val_height, val_width = image.shape[:2]
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        array_hist = [0] * 256

        for jj in range(val_height):
            for ii in range(val_height):
                intensity = img_gray[jj, ii]
                array_hist[intensity] += 1
        #array_hist = cv2.calcHist(img_gray, [0], None, [256], [0, 256])
        npix = val_height * val_width

        sum_low_pix = 0
        sum_high_pix = 0
        hist_low = 0
        hist_high = 255

        for ii in range(256):
            sum_low_pix += array_hist[ii]
            print (sum_low_pix)
            if sum_low_pix > npix * per_low / 100:
                hist_low = ii
                break

        for ii in range(256):
            sum_high_pix += array_hist[255-ii]
            print (sum_high_pix)
            if sum_high_pix > npix * per_high / 100:
                hist_high = ii
                break

        return (hist_low, hist_high)

    @staticmethod
    def create_stretch_LUT(low, high):
        print(low, high)
        LUT = []
        LUT.extend([0] * low)
        LUT.extend([int((x - low) / (high - low) * 255) for x in range(low, high)])
        LUT.extend([255] * (256 - high))
        return LUT

    @staticmethod
    def const_stretching(image, LUT):
        val_height, val_width = image.shape[:2]
        image_stretch = np.zeros_like(image)
        print(LUT)
        for jj in range(val_height):
            for ii in range(val_height):
                for col in range(3):
                    image.itemset((jj,ii,0),r[NDVI[i,j]][3])
                    image.itemset((jj,ii,1),r[NDVI[i,j]][2])
                    image.itemset((jj,ii,2),r[NDVI[i,j]][1])
                    image_stretch[jj, ii, col] = LUT(image[jj, ii, col])
        return image_stretch