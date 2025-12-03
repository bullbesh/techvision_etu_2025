"""
Для выполнения этой части задания используйте рисунок 1. 
Исправьте это изображение так, чтобы линии таблицы исчезли, а числа 
остались.
"""
import cv2
import math
import numpy as np


def draw_line(rho, theta, img, color=(0, 0, 255), thickness=1, linType=cv2.LINE_AA):
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)
    x0 = cos_t * rho
    y0 = sin_t * rho
    pt1 = int(x0 - 1000 * sin_t), int(y0 + 1000 * cos_t)
    pt2 = int(x0 + 1000 * sin_t), int(y0 - 1000 * cos_t)
    cv2.line(img, pt1, pt2, color, thickness, linType)

img = cv2.imread(r"D:\pythonprograms\techvision\techvision_etu_2025\src\lab4\images\1.jpg",cv2.IMREAD_GRAYSCALE)
onlyLines = cv2.Canny(img ,125, 255)
linesP = cv2.HoughLines(onlyLines, 1, np.pi/2 , 250)
for coordinates in linesP:
    draw_line(coordinates[0][0],coordinates[0][1],img,(255, 255, 255),15, cv2.LINE_AA)
cv2.namedWindow("Not Line Img",cv2.WINDOW_AUTOSIZE)
cv2.imshow("Not Line Img",img)
cv2.waitKey(5000) 