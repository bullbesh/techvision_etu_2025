"""
Используя пороговые преобразования, добиться того, чтобы 
фигура девушки попала в одну группу, а фон – в другую. 
"""
import cv2


# Открытие цветной картинки
img = cv2.imread(r"D:\pythonprograms\techvision\techvision_etu_2025\src\lab1\images\1.jpg", flags=cv2.IMREAD_GRAYSCALE)
# Создание и отображение первого окна
cv2.namedWindow("pictures", flags=cv2.WINDOW_AUTOSIZE)
cv2.imshow("pictures", img)
# Adaptive threshold
img_chbf = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 10
)
cv2.imshow("Adaptive", img_chbf)
# Пороговое преобразование
res, imgpd = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
cv2.imshow("Porog", imgpd)
print(res)
# Инвертированное пороговое преобразование
res, imgpf = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Porog_inv", imgpf)
# Бесконечное ожидание - окна закроются только при нажатии ESC
print("Нажмите ESC чтобы закрыть все окна")
while True:
    key = cv2.waitKey(0)
    if key == 27: # Код клавиши ESC
        break
cv2.destroyAllWindows()