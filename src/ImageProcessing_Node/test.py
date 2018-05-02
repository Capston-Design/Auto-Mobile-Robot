#!/usr/bin/env python
import numpy as np
import os
import cv2


class FeatureMatching:
    def __init__(self):
        self.path = os.getcwd() + "/data"
        self.compare_img = dict(traffic=cv2.imread(self.path + "/card1.jpg"),
                                parking=cv2.imread(self.path + "/card2.jpg"),
                                crossbar=cv2.imread(self.path + "/card3.jpg"),
                                tunnel=cv2.imread(self.path + "/card4.jpg"))
        self.src_kp = None
        self.src_des = None
        self.kp = dict(kp1=[], kp2=[], kp3=[], kp4=[])
        self.des = dict(des1=[], des2=[], des3=[], des4=[])
        self.matches = dict(match1=[], match2=[], match3=[], match4=[])
        self.good = dict(good1=[], good2=[], good3=[], good4=[])

        self.sift = cv2.xfeatures2d.SIFT_create()
        self.set_flann()

    def fn_clear(self):
        for i in range(1, 5):
            self.good['good' + str(i)].clear()

    def fn_calc_mse(self, src_pts, dst_pts):
        squared_diff = (src_pts - dst_pts) ** 2
        sum = np.sum(squared_diff)
        num_all = src_pts.shape[0] * src_pts.shape[1]
        err = sum / num_all

        return err

    def set_flann(self):
        for key in self.compare_img.keys():
            if key == 'traffic':
                self.kp['kp1'] = self.sift.detectAndCompute(self.compare_img[key], None)[0]
                self.des['des1'] = self.sift.detectAndCompute(self.compare_img[key], None)[1]
            elif key == 'parking':
                self.kp['kp2'] = self.sift.detectAndCompute(self.compare_img[key], None)[0]
                self.des['des2'] = self.sift.detectAndCompute(self.compare_img[key], None)[1]
            elif key == 'crossbar':
                self.kp['kp3'] = self.sift.detectAndCompute(self.compare_img[key], None)[0]
                self.des['des3'] = self.sift.detectAndCompute(self.compare_img[key], None)[1]
            elif key == 'tunnel':
                self.kp['kp4'] = self.sift.detectAndCompute(self.compare_img[key], None)[0]
                self.des['des4'] = self.sift.detectAndCompute(self.compare_img[key], None)[1]
            else:
                return

        FLANN_INDEX_KDTEE = 0
        index_params = dict(algorithm=FLANN_INDEX_KDTEE, trees=5)
        search_params = dict(checks=50)
        self.flann = cv2.FlannBasedMatcher(index_params, search_params)

    def fn_flann(self, frame):
        self.src_kp, self.src_des = self.sift.detectAndCompute(frame, None)

        for key in self.compare_img.keys():
            if key == 'traffic':
                self.matches['match1'] = self.flann.knnMatch(self.src_des, self.des['des1'], k=2)
            elif key == 'parking':
                self.matches['match2'] = self.flann.knnMatch(self.src_des, self.des['des2'], k=2)
            elif key == 'crossbar':
                self.matches['match3'] = self.flann.knnMatch(self.src_des, self.des['des3'], k=2)
            elif key == 'tunnel':
                self.matches['match4'] = self.flann.knnMatch(self.src_des, self.des['des4'], k=2)
            else:
                return

        for key in self.matches.keys():
            for m, n in self.matches[key]:
                if m.distance < 0.55 * n.distance:
                    if key == 'match1':
                        self.good['good1'].append(m)
                    elif key == 'match2':
                        self.good['good2'].append(m)
                    elif key == 'match3':
                        self.good['good3'].append(m)
                    elif key == 'match4':
                        self.good['good4'].append(m)
                    else:
                        return

    def run(self):
        if self.path is None:
            print("[WARNING] No such file was found", end="")
            exit()
        try:
            cap = cv2.VideoCapture(0)
            cap.set(3, 320)
            cap.set(4, 240)

        except Exception as e:
            print(e)

        else:
            while cap.isOpened():
                ret, frame = cap.read()
                if ret:
                    self.fn_flann(frame)
                    result = None
                    if len(self.good['good1']) > 7:
                        src_pts = np.float32([self.src_kp[m.queryIdx].pt for m in self.good['good1']]).reshape(-1, 1, 2)
                        dst_pts = np.float32([self.kp['kp1'][m.trainIdx].pt for m in self.good['good1']]).reshape(-1, 1, 2)
                        mse = self.fn_calc_mse(src_pts, dst_pts)
                        if mse < 40000:
                            print("card1 Detect")
                            result = cv2.drawMatches(frame, self.src_kp, self.compare_img['traffic'], self.kp['kp1'],
                                                     self.good['good1'], result, flags=2)

                    elif len(self.good['good2']) > 7:
                        src_pts = np.float32([self.src_kp[m.queryIdx].pt for m in self.good['good2']]).reshape(-1, 1, 2)
                        dst_pts = np.float32([self.kp['kp2'][m.trainIdx].pt for m in self.good['good2']]).reshape(-1, 1, 2)
                        mse = self.fn_calc_mse(src_pts, dst_pts)
                        if mse < 40000:
                            print("card2 Detect")
                            result = cv2.drawMatches(frame, self.src_kp, self.compare_img['parking'], self.kp['kp2'],
                                                     self.good['good2'], result, flags=2)

                    elif len(self.good['good3']) > 7:
                        src_pts = np.float32([self.src_kp[m.queryIdx].pt for m in self.good['good3']]).reshape(-1, 1, 2)
                        dst_pts = np.float32([self.kp['kp3'][m.trainIdx].pt for m in self.good['good3']]).reshape(-1, 1, 2)
                        mse = self.fn_calc_mse(src_pts, dst_pts)
                        if mse < 40000:
                            print("card3 Detect")
                            result = cv2.drawMatches(frame, self.src_kp, self.compare_img['crossbar'], self.kp['kp3'],
                                                     self.good['good3'], result, flags=2)

                    elif len(self.good['good4']) > 7:
                        src_pts = np.float32([self.src_kp[m.queryIdx].pt for m in self.good['good4']]).reshape(-1, 1, 2)
                        dst_pts = np.float32([self.kp['kp4'][m.trainIdx].pt for m in self.good['good4']]).reshape(-1, 1, 2)
                        mse = self.fn_calc_mse(src_pts, dst_pts)
                        if mse < 40000:
                            print("card4 Detect")
                            result = cv2.drawMatches(frame, self.src_kp, self.compare_img['tunnel'], self.kp['kp4'],
                                                     self.good['good4'], result, flags=2)
                    if result is None:
                        pass
                    else:
                        cv2.imshow("Result", result)
                    self.fn_clear()

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

            cap.release()
            cv2.destroyAllWindows()


if __name__ == '__main__':
    cls = FeatureMatching()
    cls.run()
