"""
Для выполнения этого задания используйте картинки 4_5_1 - 4_5_6.   
Найдите любые три круглых дорожных знака. 
"""
import cv2
import numpy as np


img = cv2.imread(r"D:\pythonprograms\techvision\techvision_etu_2025\src\lab4\images\6.jpg",cv2.IMREAD_REDUCED_GRAYSCALE_4)
kernel = np.ones((3,3),np.uint8)
img_n = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel,iterations=2)
onlyLinesCircles = cv2.Canny(img_n ,50, 255)
onlyLinesCircles = cv2.GaussianBlur(onlyLinesCircles, (5, 5), 0)
circlesP = cv2.HoughCircles(onlyLinesCircles, cv2.HOUGH_GRADIENT, dp=1, minDist=25, param1=255, param2=75, minRadius=5)
maxIndexCircle = 0
maxRadCircle = 0
for i in range(len(circlesP)):
    if maxRadCircle < circlesP[i][0][2]:
        maxRadCircle = circlesP[i][0][2]
        maxIndexCircle = i

cv2.circle(img,
           (int(circlesP[maxIndexCircle][0][0]), int(circlesP[maxIndexCircle][0][1])),
           int(circlesP[maxIndexCircle][0][2]),
           (0, 0, 255), 
           2
)

cv2.namedWindow("Window",cv2.WINDOW_AUTOSIZE)
cv2.imshow("Window",img)
cv2.waitKey(1000)

img2 = cv2.imread(r"D:\pythonprograms\techvision\techvision_etu_2025\src\lab4\images\5.jpg", cv2.IMREAD_REDUCED_GRAYSCALE_4)
img_n2 = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel, iterations=2)
onlyLinesCircles2 = cv2.Canny(img_n2, 50, 255)
onlyLinesCircles2 = cv2.GaussianBlur(onlyLinesCircles2, (5, 5), 0)
circlesP2 = cv2.HoughCircles(onlyLinesCircles2, cv2.HOUGH_GRADIENT, dp=1, minDist=25, param1=255, param2=75, minRadius=5)
if circlesP2 is not None:
    circlesP2 = circlesP2[0] 
    maxIndexCircle2 = 0
    maxRadCircle2 = 0
    for i in range(len(circlesP2)):
        if maxRadCircle2 < circlesP2[i][2]:
            maxRadCircle2 = circlesP2[i][2]
            maxIndexCircle2 = i
cv2.circle(img2, (int(circlesP2[maxIndexCircle2][0]), int(circlesP2[maxIndexCircle2][1])), int(circlesP2[maxIndexCircle2][2]), (0, 0, 0), 2)
cv2.namedWindow("Window2", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Window2", img2)
cv2.waitKey(1000)

img3 = cv2.imread(r"D:\pythonprograms\techvision\techvision_etu_2025\src\lab4\images\3.jpg",cv2.IMREAD_REDUCED_GRAYSCALE_4)
img_n3 = cv2.morphologyEx(img3, cv2.MORPH_CLOSE, kernel,iterations=2)
onlyLinesCircles3 = cv2.Canny(img_n3 ,50, 255)
onlyLinesCircles3 = cv2.GaussianBlur(onlyLinesCircles3, (5, 5), 0)
circlesP = cv2.HoughCircles(onlyLinesCircles3, cv2.HOUGH_GRADIENT, dp=1, minDist=25, param1=255, param2=75, minRadius=5)
for i in range(len(circlesP)):
    if maxRadCircle < circlesP[i][0][2]:
        maxRadCircle = circlesP[i][0][2]
        maxIndexCircle = i
cv2.circle(img3, (int(circlesP[maxIndexCircle][0][0]),int(circlesP[maxIndexCircle][0][1])), int(circlesP[maxIndexCircle][0][2]), (0, 0, 0), 2)
cv2.namedWindow("Window3", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Window3", img3)
cv2.waitKey(1000)
