"""
Используя пороговые преобразования, добиться того, чтобы 
горы попали в одну группу, а фон – в другую. (изображение 1-3) Какая 
функция для этого подошла лучше всего? Ручной поиск, адаптивный или 
автоматический? 
"""
import cv2
import numpy as np


# Загрузка изображения
img = cv2.imread(r"D:\pythonprograms\techvision\techvision_etu_2025\src\lab1\images\3.png", cv2.IMREAD_COLOR)
# Конвертируем в grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 1. РУЧНОЙ ПОРОГ (подбираем значение)
manual_threshold = 150 # Подбираем значение для лучшего разделения
ret, manual_result = cv2.threshold(
    img_gray,
    manual_threshold,
    255,
    cv2.THRESH_BINARY_INV # Инвертируем, чтобы горы были белыми
)
cv2.imshow("Manual Threshold", manual_result)
cv2.waitKey(100)
# 2. АДАПТИВНЫЙ ПОРОГ
adaptive_result = cv2.adaptiveThreshold(
    img_gray,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY_INV, # Инвертируем
    15, # Размер блока
    5 # Константа
)
cv2.imshow("Adaptive Threshold", adaptive_result)
cv2.waitKey(100)
13
# 3. АВТОМАТИЧЕСКИЙ ПОРОГ (Оцу)
ret2, otsu_result = cv2.threshold(
    img_gray,
    0, # Порог игнорируется при использовании Оцу
    255,
    cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU # Метод Оцу + инверсия
)
cv2.imshow("Otsu Threshold", otsu_result)
cv2.waitKey(100)
# Адаптивный mean
adaptive_mean = cv2.adaptiveThreshold(
    img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 15, 5
)
# Адаптивный gaussian с другими параметрами
adaptive_gauss2 = cv2.adaptiveThreshold(
    img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 10
)
cv2.imshow("Adaptive Mean", adaptive_mean)
cv2.waitKey(100)
cv2.imshow("Adaptive Gauss2", adaptive_gauss2)
cv2.waitKey(10000)