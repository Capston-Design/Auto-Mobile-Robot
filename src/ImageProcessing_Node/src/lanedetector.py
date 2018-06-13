#!/usr/bin/env python
# -*-coding:utf-8-*-
import numpy as np
import cv2
import time


class LaneDetector:
    # 기본변수 셋팅 후 전처리를 진행하는 생성자
    def __init__(self, info):
        # 원본 이미지 관련 변수
        self.__src_height, self.__src_width = info[:2]

        # Perspective 이미지 관련 변수
        self.__ratio = (1, 1)
        self.__pers_height = int(self.__src_height * self.__ratio[0])
        self.__pers_width = int(self.__src_width * self.__ratio[1])
        self.__init_position = np.float32([[40, 0], [0, 99], [430, 0], [480, 99]])
        self.__trans_position = np.float32([[50, 0], [40, 99], [420, 0], [440, 99]])

        # 차선 예외처리 관련 변수
        self.__lane_to_center = self.__src_width // 2 - 80

        # 이미지 처리과정을 보여주는 변수
        self.process = []

        # 전처리에 필요한 도구를 만드는 변수와 메소드(가로선, 네비게이터)
        self.__num_of_section = 10
        self.__horizon_image, self.__navigator_image = self._set_tools()

    # 차선인식에 필요한 도구를 만드는 메소드
    def _set_tools(self):
        # 가로선 마스크 이미지를 생성
        horizon = np.zeros((self.__src_height, self.__src_width), np.uint8)
        offset = int(round(self.__src_height / self.__num_of_section))
        pre_pos = 0
        for i in range(0, self.__num_of_section):
            horizon = cv2.line(horizon, (0, pre_pos + offset), (self.__src_width, pre_pos + offset), 255, 1)
            pre_pos += offset

        # 기준선 이미지를 생성
        navigator = np.zeros((self.__src_height, self.__src_width, 3), np.uint8)
        cnt_point = (self.__src_width // 2, self.__src_height // 2)
        cv2.line(navigator, (cnt_point[0], cnt_point[1] - 10),
                 (cnt_point[0], cnt_point[1] + 10), (255, 0, 0), 2)
        cv2.line(navigator, (cnt_point[0] - 100, cnt_point[1]),
                 (cnt_point[0] + 100, cnt_point[1]), (255, 0, 0), 2)
        cv2.line(navigator, (cnt_point[0] - 100, cnt_point[1] - 5),
                 (cnt_point[0] - 100, cnt_point[1] + 5), (255, 0, 0), 2)
        cv2.line(navigator, (cnt_point[0] + 100, cnt_point[1] - 5),
                 (cnt_point[0] + 100, cnt_point[1] + 5), (255, 0, 0), 2)
        return horizon, navigator

    # 결과이미지를 만드는 메소드
    def _set_tools_navigation(self, src, value):
        navigator = self.__navigator_image.copy()

        mask = cv2.line(navigator, (value, self.__src_height // 2 - 5),
                        (value, self.__src_height // 2 + 5), (255, 0, 255), 1)
        mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
        __, mask = cv2.threshold(mask, 10, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)

        img1 = cv2.bitwise_and(src, src, mask=mask_inv)
        img2 = cv2.bitwise_and(navigator, navigator, mask=mask)
        img = cv2.add(img1, img2)
        return img

    # 전처리를 실행하는 메소드
    def __call__(self, src, fps):
        # 원본 이미지 복사
        frame = src.copy()
        self.process.append(["Source Image", frame])

        # 그레이 이미지 변환
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        self.process.append(["Gray Image", frame])

        # 이진화 이미지 변환
        __, frame = cv2.threshold(frame, 190, 255, cv2.THRESH_BINARY)
        self.process.append(["Threshold Image", frame])

        # Canny 이미지 변환
        frame = cv2.Canny(frame, 150, 200, apertureSize=7)
        self.process.append(["Canny Image", frame])

        # Perspective 이미지 변환
        tmp = cv2.getPerspectiveTransform(self.__init_position, self.__trans_position)
        frame = cv2.warpPerspective(frame, tmp, (self.__pers_width, self.__pers_height))
        self.process.append(["Perspective Image", frame])

        # Canny 이미지와 Horizon 이미지의 교차점 탐색
        frame = cv2.bitwise_and(frame, self.__horizon_image)
        self.process.append(["Dot Image", frame])

        # frame[0]: 좌, frame[1]: 중앙선, frame[2]: 우 좌우의
        # 좌우에서 각 행별 중앙선에 가까운 픽셀을 탐색해 사전 형태로 저장
        frame = np.hsplit(frame, [self.__src_width // 2, self.__src_width // 2 + 1])
        pxl_info = [dict({i: np.argwhere(frame[0][i]).transpose().reshape(-1) for i in range(0, self.__src_height)}),
                    dict({i: np.argwhere(frame[2][i]).transpose().reshape(-1) for i in range(0, self.__src_height)})]
        for i, info in enumerate(pxl_info):
            tmp = info.copy()
            for key in info:
                if len(info[key]) == 0:
                    tmp.pop(key)
                else:
                    if i == 0:
                        tmp[key] = max(info[key])
                    else:
                        tmp[key] = min(info[key])
            pxl_info[i] = tmp

        # If -> 좌우측의 차선이 모두 검출되는 경우 중앙값 구하기
        # Else -> 좌측 또는 우측의 차선이 검출되지 않을 경우의 예외처리
        center = dict()
        if len(pxl_info[0]) >= 3 and len(pxl_info[1]) >= 3:
            # TODO: pxl_info[0]과 pxl_info[1]의 같은 행에 값이 존재하는 경우
            for key in pxl_info[0]:
                if pxl_info[1].get(key) is not None:
                    center.update({key: (pxl_info[0][key] + (self.__src_width // 2 + pxl_info[1][key])) // 2})
            # TODO: pxl_info[0]과 pxl_info[1]의 같은 행에 값이 존재하지 않는 경우
        else:
            if len(pxl_info[1]) < 3 <= len(pxl_info[0]):
                for key in pxl_info[0]:
                    center.update({key: pxl_info[0][key] + self.__lane_to_center})
            elif len(pxl_info[0]) < 3 <= len(pxl_info[1]):
                for key in pxl_info[1]:
                    center.update({key: (self.__src_width // 2 + pxl_info[1][key]) - self.__lane_to_center})
            else:
                print("[WARNING]Lane not found")
                err = 0
                fps = "FPS : %0.1f" % fps
                frame = cv2.add(src, self.__navigator_image)
                cv2.putText(frame, fps, (10, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
                self.process.append(["Result Image", frame])
                return err

        val = int(np.mean(np.array(list(center.values()))))
        err = val - self.__src_width // 2
        fps = "FPS : %0.1f" % fps
        frame = self._set_tools_navigation(src, val)
        cv2.putText(frame, fps, (10, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        self.process.append(["Result Image", frame])
        return err


if __name__ == '__main__':
    node = LaneDetector((40, 480))
    cap = cv2.VideoCapture(0)

    prev_time = 0
    while cap.isOpened():
        ret, fm = cap.read()
        fm = cv2.resize(fm, (480, 100))
        fm = fm[60:, :, :]

        # FPS 를 구하는 과정
        cur_time = time.time()
        f = 1 / (cur_time - prev_time)
        prev_time = cur_time

        # 결과 이미지 출력 및 Error 출력
        pre_t = time.time()
        error = node(fm, f)
        print(str(round(time.time() - pre_t, 6)) + "(초)")

        # 처리과정 이미지 출력
        for process in node.process:
            cv2.imshow(process[0], process[1])
        node.process.clear()

        if cv2.waitKey(1) and 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


