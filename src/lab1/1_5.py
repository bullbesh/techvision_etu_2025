"""
Для выполнения этого задания используйте изображение 1-4. 
Примените к нему все известные вам фильтры для сглаживания 
изображений. 
Определите, какие из них больше всего подходят для того, чтобы 
максимально убрать все неровности на изображениях.
"""
import cv2
import numpy as np


# Загрузка изображения
img = cv2.imread(r"D:\pythonprograms\techvision\techvision_etu_2025\src\lab1\images\4.png", cv2.IMREAD_COLOR)
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
ksize = (15, 15) # размер ядра размытия
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
ksize = 15
# Медианный фильтр
img_new = cv2.medianBlur(
    img, # входное изображение
    ksize # размер ядра
)
cv2.imshow("Median Blur", img_new)
cv2.waitKey(1000)
cv2.destroyAllWindows()
# Параметры для bilateralFilter
d = 15 # диаметр окрестности каждого пикселя
sigmaColor = 75 # фильтр sigma в цветовом пространстве
sigmaSpace = 75 # фильтр sigma в координатном пространстве
borderType = cv2.BORDER_DEFAULT # тип границы
# Применение bilateralFilter
img_new = cv2.bilateralFilter(
    img, # входное изображение
    d, # размер окрестности пикселя
    sigmaColor, # ширина второго компонента весовой функции (по цвету)
    sigmaSpace, # ширина первого компонента весовой функции (по пространству)
    borderType # тип рамки
)
# Показать результаты
cv2.imshow("Original", img)
cv2.imshow("Bilateral Filter", img_new)
cv2.waitKey(10000)
cv2.destroyAllWindows()