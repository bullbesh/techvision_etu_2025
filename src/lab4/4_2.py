"""
Для выполнения этого задания используйте обработанное операцией 
размыкания изображение из работы 2. На нём найдите самый длинный 
отрезок и самую большую окружность.
"""
import cv2
import math
import numpy as np


def draw_line_P(x0, y0, x1, y1, img, color=(0, 0, 255),thickness=1, lineType=cv2.LINE_AA):
    cv2.line(img, (x0, y0), (x1, y1),color, thickness, lineType)

img = cv2.imread(r"D:\pythonprograms\techvision\techvision_etu_2025\src\lab4\images\321.jpg")
kernel = np.ones((3,3),np.uint8)
img_n = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel,iterations=2)
onlyLinesCircles = cv2.Canny(img_n ,50, 255)
onlyLinesCircles = cv2.GaussianBlur(onlyLinesCircles, (5, 5), 0)

linesP = cv2.HoughLinesP(
    onlyLinesCircles, 1, np.pi / 180, 150, minLineLength=80
)

circlesP = cv2.HoughCircles(
    onlyLinesCircles,
    cv2.HOUGH_GRADIENT,
    dp=1,
    minDist=25,
    param1=255,
    param2=75,
    minRadius=5
)
maxIndexLine = 0
maxLenLine = 0
maxIndexCircle = 0
maxRadCircle = 0
for i in range(len(linesP)):
    if maxLenLine < math.sqrt((linesP[i][0][0] - linesP[i][0][2])**2 + (linesP[i][0][1] - linesP[i][0][3])**2):
        maxLenLine = math.sqrt((linesP[i][0][0] - linesP[i][0][2])**2 + (linesP[i][0][1] - linesP[i][0][3])**2)
        maxIndexLine = i
for i in range(len(circlesP)):
    if maxRadCircle < circlesP[i][0][2]:
        maxRadCircle = circlesP[i][0][2]
        maxIndexCircle = i
cv2.circle(img_n, (int(circlesP[maxIndexCircle][0][0]),int(circlesP[maxIndexCircle][0][1])),
int(circlesP[maxIndexCircle][0][2]), (255, 0, 0), 2)
draw_line_P(linesP[maxIndexLine][0][0],linesP[maxIndexLine][0][1],linesP[maxIndexLine][0][2],linesP[maxIndexLine][0][3],img_n,(255, 0, 0), 4 , cv2.LINE_AA)
cv2.namedWindow("Biggest Line and Circle",cv2.WINDOW_AUTOSIZE)
cv2.imshow("Biggest Line and Circle",img_n)
cv2.waitKey(5000)