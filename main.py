import cv2
import numpy as np
import time

video_name = 1
cap = cv2.VideoCapture(video_name)
while True:
    ret, frame = cap.read()

    frame_show = frame
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_blur = cv2.GaussianBlur(frame, (5, 5), 0)  # 高斯
    ret, frame_otsu = cv2.threshold(frame_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # 需要额外处理，图像不同位置采用不同阈值分割,C.md中第一点，改成自适应阈值

    for pixel_y in range(frame_otsu.shape[0], 0, -1):
        for pixel_x in range(frame_otsu.shape[1] // 2, 0, -1):  # 从中间往左边
            if pixel_x == 0:
                cv2.circle(frame_show, (pixel_x, pixel_y), 2, (0, 0, 255), -1)
                break
            if frame_otsu[pixel_x][pixel_y] == 255 and frame_otsu[pixel_x - 1][pixel_y] - 1 == 0 and \
                    frame_otsu[pixel_x + 1][pixel_y] == 255:
                cv2.circle(frame_show, (pixel_x, pixel_y), 2, (0, 0, 255), -1)
                break
        for pixel_x in range(frame_otsu.shape[1] // 2, frame_otsu.shape[1], 1):  # 从中间往右边
            if pixel_x == frame_otsu.shape[1] - 1:
                cv2.circle(frame_show, (pixel_x, pixel_y), 2, (0, 0, 255), -1)
                break
            if frame_otsu[pixel_x][pixel_y] == 255 and frame_otsu[pixel_x - 1][pixel_y] - 1 == 0 and \
                    frame_otsu[pixel_x + 1][pixel_y] == 255:
                cv2.circle(frame_show, (pixel_x, pixel_y), 2, (0, 0, 255), -1)
                break








