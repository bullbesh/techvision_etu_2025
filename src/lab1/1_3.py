"""
Выделить разметку на изображении 1-2
"""
import cv2


# Открытие цветной картинки
img = cv2.imread(r"D:\pythonprograms\techvision\techvision_etu_2025\src\lab1\images\1.jpg", flags=cv2.IMREAD_GRAYSCALE)
# Создание и отображение первого окна
cv2.namedWindow("pictures", flags=cv2.WINDOW_AUTOSIZE)
cv2.imshow("pictures", img)
# Пороговое преобразование
res, imgpd = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
cv2.imshow("Porog", imgpd)
# Инвертированное пороговое преобразование
res, imgpf = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY_INV)
11
cv2.imshow("Porog_inv", imgpf)
while True:
    key = cv2.waitKey(0)
    if key == 27: # Код клавиши ESC
        break
cv2.destroyAllWindows()