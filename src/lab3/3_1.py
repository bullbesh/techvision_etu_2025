"""
Протестировать работу оператора Собеля на изображениях клетки 
(вертикальные и горизонтальные линии) и косой штриховки.  
Протестировать работу фильтра Лапласа на тех же изображениях.
"""
import cv2 
import numpy as np


#Открытие чб картинки на 7 секунд
img1 = cv2.imread(
    r"D:\pythonprograms\techvision\techvision_etu_2025\src\lab3\images\1.jpg", # путь до изображения
    flags=cv2.IMREAD_REDUCED_GRAYSCALE_4 # параметр(ы) чтения
)
img2 = cv2.imread(
    r"D:\pythonprograms\techvision\techvision_etu_2025\src\lab3\images\2.jpg", # путь до изображения
    flags=cv2.IMREAD_REDUCED_GRAYSCALE_4 # параметр(ы) чтения
)
img3 = cv2.imread(
    r"D:\pythonprograms\techvision\techvision_etu_2025\src\lab3\images\3.jpg", # путь до изображения
    flags=cv2.WINDOW_AUTOSIZE # параметр(ы) чтения
)
#Создание окна для отображения:
cv2.namedWindow(
    "chb1", # имя окна
    flags=cv2.WINDOW_AUTOSIZE # параметр(ы) окна
)
#Отображение изображения в окне:
cv2.imshow(
    "chb1", # имя окна
    img1 # переменная, содержащая изображение
)
#Функция ожидания нажатия на клавишу:
key = cv2.waitKey(
    2000 # время ожидания нажатия
)
#Закрытие окна:
cv2.destroyWindow (
    "chb1" # имя окна
)
sob1 = cv2.Sobel (
    img1, # исходное изображение
    cv2.CV_64F, # глубина х2
    dx=0, # порядок производной по X
    dy=1, # порядок производной по Y
    ksize=3, # размер ядра
    scale=1, # масштаб
    delta=0, # смещение
    borderType=cv2.BORDER_DEFAULT # тип границы
)

dst1 = cv2.Laplacian(
    img1, # исходное изображение
    cv2.CV_64F, # глубина х2
    ksize=5, # размер ядра
    scale=2, # масштаб
    delta=0, # смещение 
    borderType=cv2.BORDER_DEFAULT # тип границы
)

cv2.imshow(
    "chb1",
    sob1
)

key = cv2.waitKey(
    2000 # время ожидания нажатия
)
cv2.destroyAllWindows()
#--------------------------------------------------------------------
#Создание окна для отображения:
cv2.namedWindow(
    "chb2", # имя окна
    flags=cv2.WINDOW_AUTOSIZE # параметр(ы) окна
)
#Отображение изображения в окне:
cv2.imshow(
    "chb2", # имя окна
    img2 # переменная, содержащая изображение
)
#Функция ожидания нажатия на клавишу:
key = cv2.waitKey(
    2000 # время ожидания нажатия
)
#Закрытие окна:
cv2.destroyWindow (
    "chb2" # имя окна
)

dst2 = cv2.Laplacian(
    img2, # исходное изображение
    cv2.CV_64F, # глубина х2
    ksize=5, # размер ядра
    scale=2, # масштаб
    delta=50, # смещение
    borderType=cv2.BORDER_DEFAULT # тип границы
)

cv2.imshow(
    "chb2",
    dst2
)

key = cv2.waitKey(
    2000 # время ожидания нажатия
)
cv2.destroyAllWindows()


#Создание окна для отображения:
cv2.namedWindow(
    "chb3", # имя окна
    flags=cv2.WINDOW_AUTOSIZE # параметр(ы) окна
)
#Отображение изображения в окне:
cv2.imshow(
    "chb3", # имя окна
    img3 # переменная, содержащая изображение
)
#Функция ожидания нажатия на клавишу:
key = cv2.waitKey(
    2000 # время ожидания нажатия
)
#Закрытие окна:
cv2.destroyWindow (
    "chb3" # имя окна
)

dst3 = cv2.Laplacian(
    img3, # исходное изображение
    cv2.CV_64F, # глубина х2
    ksize=5, # размер ядра
    scale=0.5, # масштаб
    delta=0, # смещение
    borderType=cv2.BORDER_DEFAULT # тип границы
)

cv2.imshow(
    "chb3",
    dst3
)

key = cv2.waitKey(
    2000 # время ожидания нажатия
)

cv2.waitKey(0)
cv2.destroyAllWindows()