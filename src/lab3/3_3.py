"""
Протестировать работу оператора Кенни, фильтра Лапласа
"""
import cv2 
import numpy as np


#Открытие чб картинки на 7 секунд
img = cv2.imread(
    r"C:\Users\Blonda\Desktop\tz\3\5.jpg", # путь до изображения
    flags=cv2.IMREAD_COLOR # параметр(ы) чтения
)
#Создание окна для отображения:
cv2.namedWindow(
    "chb1", # имя окна
    flags=cv2.WINDOW_AUTOSIZE # параметр(ы) окна
)
#Отображение изображения в окне:
cv2.imshow(
    "chb1", # имя окна
    img # переменная, содержащая изображение
)
#Функция ожидания нажатия на клавишу:
key = cv2.waitKey(
    2000 # время ожидания нажатия
)
#Закрытие окна:
cv2.destroyWindow (
    "chb1" # имя окна
)

edges = cv2.Canny(
    img, # входное изображение
    255, # нижний порог
    255, # верхний порог
    apertureSize=3, # размер ядра
    L2gradient=False # вычисление нормы L2
)
cv2.imshow(
    "chb1",
    edges
)

key = cv2.waitKey(
    2000 # время ожидания нажатия
)

dst1 = cv2.Laplacian(
    edges, # исходное изображение
    cv2.CV_64F, # глубина х2
    ksize=5, # размер ядра
    scale=2, # масштаб
    delta=0, # смещение
    borderType=cv2.BORDER_DEFAULT # тип границы
)

cv2.imshow(
    "chb1",
    dst1
)

key = cv2.waitKey(
    2000 # время ожидания нажатия
)

cv2.waitKey(0)
cv2.destroyAllWindows()