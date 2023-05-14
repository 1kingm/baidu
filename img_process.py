import time
import cv2
import numpy as np

frame = cv2.imread('img/5.png')
frame = cv2.resize(frame, (320, 240))
frame_show = frame
frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
frame_blur = cv2.GaussianBlur(frame_gray, (5, 5), 0)  # 高斯
ret, frame_otsu = cv2.threshold(frame_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# 边界突变
start = time.time()
line_mid = []
line_left = []
line_right = []


# 255白色， 0黑色

def Mutant(x):
    dot = []
    for i in range(0, len(x) - 1):
        if (x[i] - x[i + 1]) // (x[i] - x[i - 1] + 0.01) < -100 or (x[i] - x[i + 1]) // (x[i] - x[i - 1] + 0.01) > 100:
            dot.extend([x[i], frame.shape[0] - x.index(x[i])])
        # dot.append((x[i] - x[i - 1]) // (x[i] - x[i + 1] + 0.01))
    return dot


for pixel_y in range(frame_otsu.shape[0] - 1, -1, -1):  # 从479到0
    for pixel_x1 in range(frame_otsu.shape[1] // 2 - 1, -1, -1):  # 从中间往左边,319到0
        if pixel_x1 == 0:
            cv2.circle(frame_show, (pixel_x1, pixel_y), 2, (0, 0, 255), -1)
            break
        if frame_otsu[pixel_y, pixel_x1] == 255 and frame_otsu[pixel_y, pixel_x1 - 1] == 0:
            cv2.circle(frame_show, (pixel_x1, pixel_y), 2, (0, 0, 255), -1)
            break
    for pixel_x2 in range(frame_otsu.shape[1] // 2, frame_otsu.shape[1], 1):  # 从中间往右边
        if pixel_x2 == frame_otsu.shape[1] - 1:  # 638中止
            cv2.circle(frame_show, (pixel_x2, pixel_y), 2, (0, 0, 255), -1)
            break
        if frame_otsu[pixel_y, pixel_x2 - 1] == 255 and frame_otsu[pixel_y, pixel_x2] == 0:
            cv2.circle(frame_show, (pixel_x2, pixel_y), 2, (0, 0, 255), -1)
            break
    cv2.circle(frame_show, ((pixel_x2 + pixel_x1) // 2, pixel_y), 2, (255, 0, 0), -1)
    line_left.append(pixel_x1)
    line_right.append(pixel_x2)
    line_mid.append((pixel_x2 + pixel_x1) // 2)
dot = Mutant(line_left)  # 传入为点的横坐标


# cv2.circle(frame_show, (93, 134), 2, (0, 255, 0), -1)
# cv2.circle(frame_show, (0, 119), 2, (0, 255, 0), -1)
cv2.circle(frame_show, (0, 119), 2, (0, 255, 0), -1)
print(dot)
print(time.time() - start)
cv2.imshow('frame_show', frame_show)
cv2.imshow('mask', frame_otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()
