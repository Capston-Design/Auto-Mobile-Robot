#!/usr/bin/env python
# -*-coding:utf-8-*-
import numpy as np
import time
import os
import cv2


class ObjectDetector:
    def __init__(self):
        # 이미지를 불러오는 경로에 관한 변수
        self.__path = "/home/au-di/Auto-Mobile-Robot/src/ImageProcessing_Node/data"

        # 영상에서 찾고자하는 물체이미지를 저장한 변수
        self.__obj_image = dict(traffic=cv2.imread(self.__path + "/traffic.png"),
                                parking=cv2.imread(self.__path + "/parking.png"),
                                crossbar=cv2.imread(self.__path + "/crossbar.png"),
                                tunnel=cv2.imread(self.__path + "/card4.jpg"))

        # 물체이미지에 관한 정보를 담는 변수
        self.__kp = dict(kp1=[], kp2=[], kp3=[], kp4=[])
        self.__des = dict(des1=[], des2=[], des3=[], des4=[])

        # 물체이미지의 특징점을 미리 계산해
        self.flann = self._set_tools()

    # 물체인식에 필요한 도구를 만드는 메소드
    def _set_tools(self):
        sift = cv2.xfeatures2d.SIFT_create()
        for key in self.__obj_image:
            if key == 'traffic':
                self.__kp['kp1'], self.__des['des1'] = sift.detectAndCompute(self.__obj_image[key], None)
            elif key == 'parking':
                self.__kp['kp2'], self.__des['des2'] = sift.detectAndCompute(self.__obj_image[key], None)
            elif key == 'crossbar':
                self.__kp['kp3'], self.__des['des3'] = sift.detectAndCompute(self.__obj_image[key], None)
            elif key == 'tunnel':
                self.__kp['kp4'], self.__des['des4'] = sift.detectAndCompute(self.__obj_image[key], None)
            else:
                return

        index_params = dict(algorithm=0, trees=5)
        search_params = dict(checks=50)
        return cv2.FlannBasedMatcher(index_params, search_params)

    def __call__(self, src, fps):
        sift = cv2.xfeatures2d.SIFT_create()
        src_kp, src_des = sift.detectAndCompute(src, None)

        matches = dict()
        for key in self.__obj_image:
            if key == 'traffic':
                matches.update({'match1': self.flann.knnMatch(src_des, self.__des['des1'], k=2)})
            elif key == 'parking':
                matches.update({'match2': self.flann.knnMatch(src_des, self.__des['des2'], k=2)})
            elif key == 'crossbar':
                matches.update({'match3': self.flann.knnMatch(src_des, self.__des['des3'], k=2)})
            elif key == 'tunnel':
                matches.update({'match4': self.flann.knnMatch(src_des, self.__des['des4'], k=2)})
            else:
                return

        good = dict(good1=[], good2=[], good3=[], good4=[])
        for key in matches:
            for m, n in matches[key]:
                if m.distance < 0.7 * n.distance:
                    if key == 'match1':
                        good['good1'].append(m)
                    elif key == 'match2':
                        good['good2'].append(m)
                    elif key == 'match3':
                        good['good3'].append(m)
                    elif key == 'match4':
                        good['good4'].append(m)
                    else:
                        return

        result = [src, None]
        if len(good['good1']) > 7:
            src_pts = np.float32([src_kp[m.queryIdx].pt for m in good['good1']]).reshape(-1, 1, 2)
            dst_pts = np.float32([self.__kp['kp1'][m.trainIdx].pt for m in good['good1']]).reshape(-1, 1, 2)

            sum = np.sum((src_pts - dst_pts) ** 2)
            num_all = src_pts.shape[0] * src_pts.shape[1]
            mse = sum / num_all
            if mse < 40000:
                print("Traffic Sign Detect")
                result = [cv2.drawMatches(src, src_kp, self.__obj_image['traffic'], self.__kp['kp1'],
                                         good['good1'], None, flags=2), 'traffic']

        elif len(good['good2']) > 7:
            src_pts = np.float32([src_kp[m.queryIdx].pt for m in good['good2']]).reshape(-1, 1, 2)
            dst_pts = np.float32([self.__kp['kp2'][m.trainIdx].pt for m in good['good2']]).reshape(-1, 1, 2)

            sum = np.sum((src_pts - dst_pts) ** 2)
            num_all = src_pts.shape[0] * src_pts.shape[1]
            mse = sum / num_all
            if mse < 40000:
                print("Parking Sign Detect")
                result = [cv2.drawMatches(src, src_kp, self.__obj_image['parking'], self.__kp['kp2'],
                                         good['good2'], None, flags=2), 'parking']

        elif len(good['good3']) > 7:
            src_pts = np.float32([src_kp[m.queryIdx].pt for m in good['good3']]).reshape(-1, 1, 2)
            dst_pts = np.float32([self.__kp['kp3'][m.trainIdx].pt for m in good['good3']]).reshape(-1, 1, 2)

            sum = np.sum((src_pts - dst_pts) ** 2)
            num_all = src_pts.shape[0] * src_pts.shape[1]
            mse = sum / num_all
            if mse < 40000:
                print("Crossbar Detect")
                result = [cv2.drawMatches(src, src_kp, self.__obj_image['crossbar'], self.__kp['kp3'],
                                         good['good3'], None, flags=2), 'crossbar']

        elif len(good['good4']) > 7:
            src_pts = np.float32([src_kp[m.queryIdx].pt for m in good['good4']]).reshape(-1, 1, 2)
            dst_pts = np.float32([self.__kp['kp4'][m.trainIdx].pt for m in good['good4']]).reshape(-1, 1, 2)

            sum = np.sum((src_pts - dst_pts) ** 2)
            num_all = src_pts.shape[0] * src_pts.shape[1]
            mse = sum / num_all
            if mse < 40000:
                print("Tunnel Sign Detect")
                result = [cv2.drawMatches(src, src_kp, self.__obj_image['tunnel'], self.__kp['kp4'],
                                         good['good4'], None, flags=2), 'tunnel']
        fps = "FPS : %0.1f" % fps
        result[0] = cv2.putText(result[0], fps, (10, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        return result


if __name__ == '__main__':
    obj = ObjectDetector()
    cap = cv2.VideoCapture(0)

    prev_time = 0
    while cap.isOpened():
        ret, fm = cap.read()
        fm = cv2.resize(fm, (480, 240))

        # FPS 를 구하는 과정
        cur_time = time.time()
        f = 1 / (cur_time - prev_time)
        prev_time = cur_time

        pre_t = time.time()
        rst = obj(fm, f)
        print(str(round(time.time() - pre_t, 6)) + "(초)")

        if rst is not None:
            cv2.imshow("Result", rst)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cap.release()
    cv2.destroyAllWindows()
