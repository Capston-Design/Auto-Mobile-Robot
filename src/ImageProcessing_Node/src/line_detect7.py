#!/usr/bin/env python
import rospy, cv2, cv_bridge
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
import numpy as np
import threading, time

 # 480 / 640

class Infinite_timer():
    def __init__(self, seconds, target):
        self._should_continue = False
        self.is_running = False
        self.seconds = seconds
        self.target = target
        self.thread = None

    def _handle_target(self):
        self.is_running = True
        self.target()
        self.is_running = False
        self._start_timer()

    def _start_timer(self):
        if self._should_continue:
            self.thread = threading.Timer(self.seconds, self._handle_target)
            self.thread.start()

    def start(self):
        if not self._should_continue and not self.is_running:
            self._should_continue = True
            self._start_timer()
        else:
            print("Timer already started or running, please wait if you're restarting")

    def cancle(self):
        if self.thread is not None:
            self._should_continue = False
            self.thread.cancel()
        else:
            print("Timer never started or failed to initialize")

class Follower:
    def __init__(self):
        self.bridge = cv_bridge.CvBridge()
        self.image_sub = rospy.Subscriber('/image_raw', Image, self.image_callback)
        self.cmd_vel_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
        self.twist = Twist()
        self.lasterr = 0
        self.cnt = 0
        self.is_perspective = True
        self.center_y = 370 + 130
        self.gap_pre = 200
        self.cx_pre = 392

    def image_callback(self,msg):
        #self.cnt += 1
        #if self.cnt % 3 != 0:
        #    return
        #print("start")
        video = self.bridge.imgmsg_to_cv2(msg,desired_encoding='bgr8')
        ori_height, ori_width = video.shape[:2]
        img_roi_ori = video[ori_height//2 : ori_height, :]
        img_roi = img_roi_ori.copy()
        img_resize = img_roi
        #img_resize = cv2.resize(img_roi, None, fx=0.25, fy=0.25, interpolation = cv2.INTER_NEAREST)

        if self.is_perspective:
            self.perspec_pos = self.perspective_transform(img_resize)

        h, w = img_resize.shape[:2]
        pos_pre = np.float32(self.perspec_pos[0])
        pos = np.float32(self.perspec_pos[1])
        perspective = cv2.getPerspectiveTransform(pos_pre, pos)
        img_trans = cv2.warpPerspective(img_resize, perspective, (int(w*1.2), h*2))
        img_trans_copy = img_trans.copy()

        hsv = cv2.cvtColor(img_trans,cv2.COLOR_BGR2HSV)

        # HSV_white color  [0,0,200] [255,255,255]
        # HSV_white color  [70,10,130] [180,110,255]
        lower_white = np.array([0,0,220],np.uint8)
        upper_white = np.array([255,255,255],np.uint8)
        mask_w = cv2.inRange(hsv,lower_white,upper_white)
        #white_hsv = cv2.bitwise_and(video,video,mask=mask_w)

        # HSV_Yellow color [20,100,100] [30,255,255]
        lower_yellow = np.array([20,100,100], np.uint8)
        upper_yellow = np.array([30,255,255], np.uint8)
        mask_y = cv2.inRange(hsv,lower_yellow,upper_yellow)
        #yellow_hsv = cv2.bitwise_and(video,video,mask=mask_y)

        #line = cv2.bitwise_or(white_hsv, white_hsv,mask=yellow_hsv)
        line = cv2.add(mask_w,mask_y )
        line = cv2.bitwise_and(img_trans,img_trans,mask=line)
	
         # threshold
        Gray = cv2.cvtColor(line, cv2.COLOR_BGR2GRAY)
        ret, thr = cv2.threshold(Gray, 100, 255, cv2.THRESH_BINARY)
        thr = cv2.morphologyEx(thr, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
        thr = cv2.morphologyEx(thr, cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8))

        #img_labeling = self.getLabeling(thr, 50, True)
                
        h, w = img_trans.shape[:2]
        num_v_section = int(h/4)
        v_height = h // num_v_section

        array_right_pts_x = []
        array_right_pts_y = []
        array_left_pts_x = []
        array_left_pts_y = []

        for v_section in range(num_v_section):
            v_section_top = h - (v_section + 1) * v_height
            img_v_section = thr[v_section_top:v_section_top+v_height, :]

            if np.count_nonzero(img_v_section) > 10:
                M_v = cv2.moments(img_v_section)
                if M_v['m00'] > 0:
                    v_mid = int(M_v['m10'] / M_v['m00'])
                img_v_left = img_v_section[:,:v_mid]
                img_v_right = img_v_section[:,v_mid:]

                cy = int(v_section_top + v_height/2)

                if thr[cy, v_mid] == 255 or img_trans[cy, v_mid, 0] == 0:
                    if np.count_nonzero(img_v_section) > 25:
                        cx = int(v_mid)
                        if v_mid > self.cx_pre:
                            array_right_pts_x.append(cx)
                            array_right_pts_y.append(cy)
                            cv2.circle(img_trans_copy, (cx, cy), 8, (0,255,0), 2)
                            self.cx_pre = cx - self.gap_pre
                        else:
                            array_left_pts_x.append(cx)
                            array_left_pts_y.append(cy)
                            cv2.circle(img_trans_copy, (cx, cy), 8, (0,0,255), 2)
                            self.cx_pre = cx + self.gap_pre

                else:
                    if np.count_nonzero(img_v_left) > 25 and np.count_nonzero(img_v_right) > 25:
                        M_v_left = cv2.moments(img_v_left)
                        if M_v_left['m00'] > 0:
                            cx1 = int(M_v_left['m10'] / M_v_left['m00'])
                        else:
                            cx1 = int(v_mid)

                        M_v_right = cv2.moments(img_v_right)
                        if M_v_right['m00'] > 0:
                            cx2 = int(v_mid + M_v_right['m10'] / M_v_right['m00'])
                        else:
                            cx2 = int(v_mid)

                        array_left_pts_x.append(cx1)
                        array_left_pts_y.append(cy)
                        array_right_pts_x.append(cx2)
                        array_right_pts_y.append(cy)

                        cv2.circle(img_trans_copy, (cx1, cy), 8, (0,0,255), 2)
                        cv2.circle(img_trans_copy, (cx2, cy), 8, (0,255,0), 2)
                        cv2.circle(img_trans_copy, (v_mid, cy), 8, (0,255,255), 2)

        plot_y = np.linspace(0, 2*h-1, 2*h)

        if len(array_left_pts_x) > 50 and len(array_right_pts_x) > 50:
            try:
                left_lane_fit = np.polyfit(array_left_pts_y, array_left_pts_x, 2)
                left_fit_x = left_lane_fit[0] * plot_y**2 + left_lane_fit[1] * plot_y + left_lane_fit[2]
                pts = np.array([np.transpose(np.vstack([left_fit_x, plot_y]))])
                cv2.polylines(img_trans_copy, np.int_([pts]), isClosed=False, color=(255, 0, 255), thickness = 5)

                right_lane_fit = np.polyfit(array_right_pts_y, array_right_pts_x, 2)
                right_fit_x = right_lane_fit[0] * plot_y**2 + right_lane_fit[1] * plot_y + right_lane_fit[2]
                pts = np.array([np.transpose(np.vstack([right_fit_x, plot_y]))])
                cv2.polylines(img_trans_copy, np.int_([pts]), isClosed=False, color=(255, 255, 0), thickness = 5)

                plot_x = np.mean([left_fit_x, right_fit_x], axis=0)
                pts = np.array([np.transpose(np.vstack([plot_x, plot_y]))])
                cv2.polylines(img_trans_copy, np.int_([pts]), isClosed=False, color=(255, 0, 0), thickness = 5)

                self.gap_pre = int(abs(right_fit_x[self.center_y] - plot_x[self.center_y]))
            except:
                print("fail 1")

        elif len(array_left_pts_x) > 50 and len(array_right_pts_x) <= 50:
            try:
                left_lane_fit = np.polyfit(array_left_pts_y, array_left_pts_x, 2)
                left_fit_x = left_lane_fit[0] * plot_y**2 + left_lane_fit[1] * plot_y + left_lane_fit[2]
                pts = np.array([np.transpose(np.vstack([left_fit_x, plot_y]))])
                cv2.polylines(img_trans_copy, np.int_([pts]), isClosed=False, color=(255, 0, 255), thickness = 5)

                plot_x = np.add(left_fit_x, self.gap_pre)
                pts = np.array([np.transpose(np.vstack([plot_x, plot_y]))])
                cv2.polylines(img_trans_copy, np.int_([pts]), isClosed=False, color=(255, 0, 0), thickness = 5)
            except:
                print("fail 2")

        elif len(array_left_pts_x) <= 50 and len(array_right_pts_x) > 50:
            try:
                right_lane_fit = np.polyfit(array_right_pts_y, array_right_pts_x, 2)
                right_fit_x = right_lane_fit[0] * plot_y**2 + right_lane_fit[1] * plot_y + right_lane_fit[2]
                pts = np.array([np.transpose(np.vstack([right_fit_x, plot_y]))])
                cv2.polylines(img_trans_copy, np.int_([pts]), isClosed=False, color=(255, 255, 0), thickness = 5)

                plot_x = np.subtract(right_fit_x, self.gap_pre)
                pts = np.array([np.transpose(np.vstack([plot_x, plot_y]))])
                cv2.polylines(img_trans_copy, np.int_([pts]), isClosed=False, color=(255, 0, 0), thickness = 5)
            except:
                print("fail 3")

        else:
            print("lane not pound")
            cv2.imshow('img',img_roi)
            cv2.imshow('trans',img_trans)
            cv2.imshow('threshold',thr)
            return

        if self.is_perspective:
            self.center_x = plot_x[self.center_y]
            self.is_perspective = False

        kp=0.00225
        kd=0.005
        self.cx_pre = plot_x[self.center_y]
        err = plot_x[self.center_y]-self.center_x
        print("error : {}".format(err))

        self.twist.linear.x=0.1*((1-abs(err)/192)**2)
        self.twist.angular.z = -float(kp*err+kd*(err-self.lasterr))
        self.lasterr=err
        #self.cmd_vel_pub.publish(self.twist)
        print("[INFO]end")

        cv2.imshow('img',img_roi)
        cv2.imshow('trans',img_trans)
        cv2.imshow('copy',img_trans_copy)
        cv2.imshow('threshold',thr)
        #cv2.imshow('F',img_labeling[0])
        #cv2.imshow('G',img_labeling[1])
        cv2.waitKey(3)

    def perspective_transform(self, img_resize):

        hsv = cv2.cvtColor(img_resize,cv2.COLOR_BGR2HSV)

        # HSV_white color  [0,0,200] [255,255,255]
        # HSV_white color  [70,10,130] [180,110,255]
        lower_white = np.array([0,0,230],np.uint8)
        upper_white = np.array([255,255,255],np.uint8)
        mask_w = cv2.inRange(hsv,lower_white,upper_white)
        #white_hsv = cv2.bitwise_and(video,video,mask=mask_w)

        # HSV_Yellow color [20,100,100] [30,255,255]
        lower_yellow = np.array([20,100,100], np.uint8)
        upper_yellow = np.array([30,255,255], np.uint8)
        mask_y = cv2.inRange(hsv,lower_yellow,upper_yellow)
        #yellow_hsv = cv2.bitwise_and(video,video,mask=mask_y)

        #line = cv2.bitwise_or(white_hsv, white_hsv,mask=yellow_hsv)
        line = cv2.add(mask_w,mask_y )
        line = cv2.bitwise_and(img_resize,img_resize,mask=line)

        img_height, img_width = line.shape[:2]

        img_left_w0 = 0
        img_left_h0 = img_height//4
        img_left = line[img_left_h0 : img_left_h0+(img_height//2), img_left_w0 : img_left_w0+(img_width//2)]

        img_right_w0 = img_width//2
        img_right_h0 = img_height//4
        img_right = line[img_right_h0 : img_right_h0+(img_height//2), img_right_w0 : img_right_w0+(img_width//2)]

        img_left_edges = cv2.Canny(img_left, 80, 180)
        img_right_edges = cv2.Canny(img_right, 80, 180)

        cv2.imshow('left', img_left_edges)
        cv2.imshow('right', img_right_edges)
        cv2.waitKey(3)

        img_left_lines = cv2.HoughLines(img_left_edges, 1, np.pi/180, 30)
        img_right_lines = cv2.HoughLines(img_right_edges, 1, np.pi/180, 30)

        line_left_upper_x = [rho * np.cos(theta) for [[rho, theta]] in img_left_lines[:2]]
        print(line_left_upper_x)
        line_left_ii = line_left_upper_x.index(max(line_left_upper_x))
        [[rho, theta]] = img_left_lines[line_left_ii]
        line_left = self.hough_pos(rho, theta, img_left_w0, img_left_h0, img_height)

        line_right_upper_x = [rho * np.cos(theta) for [[rho, theta]] in img_right_lines[:2]]
        print(line_right_upper_x)
        line_right_ii = line_right_upper_x.index(min(line_right_upper_x))
        [[rho, theta]] = img_right_lines[line_right_ii]
        line_right = self.hough_pos(rho, theta, img_right_w0, img_right_h0, img_height)

        ratio_w, ratio_h = 300, 350
        print (line_left, line_right)
        x_mid = (line_left[0] + line_right[0] + line_left[2] + line_right[2]) // 4 * 1.2
        x_width = ((line_left[3] + line_right[3]) - (line_left[1] + line_right[1])) * ratio_w // (4*ratio_h) * 2

        print(x_mid, x_width)

        pos1_pre = [line_left[0], line_left[1]]
        pos1 = [x_mid - x_width, line_left[1] * 2]
        pos2_pre = [line_left[2], line_left[3]]
        pos2 = [x_mid - x_width, line_left[3] * 2]
        pos3_pre = [line_right[0], line_right[1]]
        pos3 = [x_mid + x_width, line_right[1] * 2]
        pos4_pre = [line_right[2], line_right[3]]
        pos4 = [x_mid + x_width, line_right[3] * 2]

        perspective_pos_pre = [pos1_pre, pos2_pre, pos3_pre, pos4_pre]
        perspective_pos = [pos1, pos2, pos3, pos4]
        return (perspective_pos_pre, perspective_pos)

    def hough_pos(self, rho, theta, w0, h0, height):
        c_theta = np.cos(theta)
        s_theta = np.sin(theta)
        x0 = w0 + c_theta*rho
        y0 = h0 + s_theta*rho
        r1 = y0 // c_theta
        r2 = (height - y0) // c_theta
        upper_x = int(x0 - r1*(-s_theta))
        upper_y = int(y0 - r1*(c_theta))
        lower_x = int(x0 + r2*(-s_theta))
        lower_y = int(y0 + r2*(c_theta))
        return [upper_x, upper_y, lower_x, lower_y]


    def getLabeling(self, img, threshold_area, isObjWhite):
        if isObjWhite:
            objColor, backColor = 255, 0
        else:
            objColor, backColor = 0, 255
        h, w = img.shape[:2]
        Map = np.zeros_like(img)
        eq_tbl = [[0, 0]]

        label = 0
        for jj in range(1, h-1):
            for ii in range(1, w-1):
                if img[jj, ii] == objColor:
                    if (Map[jj-1, ii] != 0) and (Map[jj, ii-1] != 0):
                        if Map[jj-1, ii] == Map[jj, ii-1]:
                            Map[jj, ii] = Map[jj-1, ii]
                        else:
                            maxl = max(Map[jj-1, ii], Map[jj, ii-1])
                            minl = min(Map[jj-1, ii], Map[jj, ii-1])
                            Map[jj, ii] = minl

                            if eq_tbl[maxl][1] < eq_tbl[minl][1]:
                                min_eq = eq_tbl[maxl][1]
                            else:
                                min_eq = eq_tbl[minl][1]
                            eq_tbl[maxl][1] = min_eq
                            eq_tbl[minl][1] = min_eq
                    elif Map[jj-1, ii] != 0:
                        Map[jj, ii] = Map[jj-1, ii]
                    elif Map[jj, ii-1] != 0:
                        Map[jj, ii] = Map[jj, ii-1]
                    else:
                        label += 1
                        Map[jj, ii] = label
                        eq_tbl.append([label, label])
        for ii in range(label+1):
            temp = eq_tbl[ii][1]
            if temp != eq_tbl[ii][0]:
                eq_tbl[ii][1] = eq_tbl[temp][1]
        Hash = []
        for ii in range(label+1):
            Hash.append(0)
            Hash[eq_tbl[ii][1]] = eq_tbl[ii][1]
        cnt = 1
        for ii in range(label+1):
            if (Hash[ii] != 0):
                Hash[ii] = cnt
                cnt += 1
        for ii in range(label+1):
            eq_tbl[ii][1] = Hash[eq_tbl[ii][1]]

        newPtr = np.zeros_like(img)
        for jj in range(1, h-1):
            for ii in range(1, w-1):
                if Map[jj, ii] != 0:
                    temp = Map[jj, ii]
                    newPtr[jj, ii] = eq_tbl[temp][1]
        cnt -= 1

        ipllabel = []
        for k in range(cnt):
            npixels_label = 0
            buffimg = np.zeros_like(img)
            for jj in range(0, h):
                for ii in range(0, w):
                    if newPtr[jj, ii] == k+1:
                        buffimg[jj, ii] = objColor
                        npixels_label += 1
                    else:
                        buffimg[jj, ii] = backColor
            if npixels_label >= threshold_area:
                ipllabel.append(buffimg)
        return ipllabel

rospy.init_node('follower')
follower = Follower()
rospy.spin()
