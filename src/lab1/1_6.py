"""
Отфильтруйте изображение 1-5  так, чтобы можно было распознать 
содержимое изображения.
"""
import cv2
import numpy as np


# Загрузка изображения
img = cv2.imread(r"D:\pythonprograms\techvision\techvision_etu_2025\src\lab1\images\5.jpg", cv2.IMREAD_COLOR)
# Показать оригинальное изображение
cv2.namedWindow(
    "Original", # имя окна
    flags=cv2.WINDOW_AUTOSIZE # параметр(ы) окна
)
cv2.imshow(
    "Original", # имя окна
    img # переменная, содержащая изображение
)
cv2.waitKey(1000)
cv2.destroyAllWindows()
# Параметры для размытия
ksize = (25, 25) # размер ядра размытия
anchor = (-1, -1) # якорная точка (по умолчанию центр)
borderType = cv2.BORDER_DEFAULT # тип границы
# Применение размытия
img_new_blur = cv2.blur(
    img, # входное изображение
    ksize, # размер ядра
)
# Показать размытое изображение
cv2.namedWindow("Blurred", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Blurred", img_new_blur)
cv2.waitKey(1000)
cv2.destroyAllWindows()
# Параметры для boxFilter
ddepth = -1 # глубина такая же как у исходного изображения
ksize = (15, 15) # размер ядра
anchor = (-1, -1) # якорная точка (по умолчанию центр)
normalize = True # нормирование (рекомендуется True)
borderType = cv2.BORDER_DEFAULT # тип границы
# Применение boxFilter
img_new_filter = cv2.boxFilter(
    img, # входное изображение
    ddepth, # глубина изображения-результата
    ksize, # размер ядра
    anchor=anchor, # положение якорной точки
    normalize=normalize, # нормирование
    borderType=borderType # тип рамки
)
# Показать обработанное изображение
cv2.imshow("Box Filter", img_new_filter)
cv2.waitKey(1000)
cv2.destroyAllWindows()
ksize = (31, 31) # размер ядра (должен быть нечетным)
sigmaX = 0 # сигма по оси X (0 - вычисляется автоматически)
sigmaY = 0 # сигма по оси Y (0 - вычисляется автоматически)
borderType = cv2.BORDER_DEFAULT # тип границы
# Применение GaussianBlur
img_new = cv2.GaussianBlur(
    img, # входное изображение
    ksize, # размер ядра
    sigmaX, # сигма по оси X
    sigmaY, # сигма по оси Y
    borderType # тип рамки
)
cv2.imshow("Gaussian Blur", img_new)
cv2.waitKey(1000)
cv2.destroyAllWindows()
ksize = 31
# Медианный фильтр
img_new = cv2.medianBlur(
    img, # входное изображение
    ksize # размер ядра
)
cv2.imshow("Median Blur", img_new)
cv2.waitKey(100000)
cv2.destroyAllWindows()