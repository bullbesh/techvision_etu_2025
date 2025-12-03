"""
Для выполнения этого задания используйте изображение с 
шумом: точки на фоне или разрывы на границах.  Пример картинки 2.jpg
Примените морфологические преобразования к такому изображению так, 
чтобы максимально убрать шум в виде точек на фоне и при этом закрыть 
разрывы в линиях текста.
"""
import cv2
import numpy as np


image_path = r"D:\pythonprograms\techvision\techvision_etu_2025\src\lab2\images\2.jpg"

imgchb = cv2.imread(
    image_path,  
    flags=cv2.IMREAD_GRAYSCALE 
)

cv2.namedWindow(
    "chb",  # имя окна
    flags=cv2.WINDOW_AUTOSIZE  # параметры окна
)

cv2.imshow(
    "chb",  # имя окна
    imgchb  # переменная, содержащая изображение
)

key = cv2.waitKey(2000)  # ждем 2 секунды

image = cv2.imread(image_path)  

# Создаем ядро для морфологических операций
kernel1 = np.ones((2, 2), np.uint8)
kernel2 = np.ones((2, 2), np.uint8)


img_open = cv2.morphologyEx(
    image, 
    cv2.MORPH_OPEN, # тип операции
    kernel1, # ядро в виде массива
    iterations=2  # число итераций

    )

cv2.imshow(
    "chb",
    img_open  
)
key = cv2.waitKey(5000) 

img_close = cv2.morphologyEx(img_open, cv2.MORPH_CLOSE, kernel2, iterations=1)

cv2.imshow(
    "chb",
    img_close  
)
key = cv2.waitKey(2000) 

cv2.waitKey(0)
cv2.destroyAllWindows()