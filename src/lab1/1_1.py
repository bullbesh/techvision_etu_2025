"""
Для выполнения этого задания используйте любое изображение. Напишите 
программу, которая будет выводить изображение на экран следующим 
образом: 1. в цвете в полном размере на 5 секунд, затем закрыть; 2. в 
оттенках серого в полном размере на 7 секунд, затем закрыть; 3. в цвете в 2 
раза меньше, чем исходный размер, на 9 секунд, затем закрыть; 4. в оттенках 
серого в 4 раза меньше, чем исходный размер, на 11 секунд, затем закрыть. 5. 
В цвете в полном размере, поменяв местами зелёный и красный каналы на 4 
секунды. 6. Закрыть при нажатии на клавищу Esc. Все действия должны 
выполняться в одном скрипте.
"""
import cv2


# Загрузка изображения
img = cv2.imread(
    r"D:\pythonprograms\techvision\techvision_etu_2025\src\lab1\images\1.jpg",
    flags=cv2.IMREAD_COLOR # параметр(ы) чтения
)
# Показать оригинальное изображение
cv2.namedWindow(
    "Original", # имя окна
    flags=cv2.WINDOW_AUTOSIZE # параметр(ы) окна
)
cv2.imshow(
    "Original", # имя окна
    img # переменная, содержащая изображение
)
cv2.waitKey(5000)
cv2.destroyAllWindows()
# СЕРЫЙ
img2 = cv2.cvtColor(
    img, # входное изображение
    cv2.COLOR_BGR2GRAY # код преобразования
)
# Показать серое изображение
cv2.namedWindow(
    "Grayscale", # имя окна
    flags=cv2.WINDOW_AUTOSIZE # параметр(ы) окна
)
cv2.imshow(
    "Grayscale", # имя окна
    img2 # переменная, содержащая изображение
)
cv2.waitKey(7000)
cv2.destroyAllWindows()
#ЦВЕТ:2
# Уменьшаем изображение в 2 раза
height, width = img.shape[:2]
new_width = width // 2
new_height = height // 2
img_resized = cv2.resize(img, (new_width, new_height))
# Выводим уменьшенное изображение в окне AUTOSIZE
cv2.namedWindow("Half Size", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Half Size", img_resized)
cv2.waitKey(9000)
cv2.destroyAllWindows()
#СЕРЫЙ:4
# Уменьшаем изображение в 2 раза
height, width = img2.shape[:2]
new_width2 = width // 4
new_height2 = height // 4
img_resized2 = cv2.resize(img2, (new_width2, new_height2))
# Выводим уменьшенное изображение в окне AUTOSIZE
cv2.namedWindow("Half Size", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Half Size", img_resized2)
cv2.waitKey(11000)
cv2.destroyAllWindows()
g, b, r = cv2.split(img)
img_n = cv2.merge([g, r, b])
cv2.namedWindow(
    "Colorcheng", # имя окна
    flags=cv2.WINDOW_AUTOSIZE # параметр(ы) окна
)
cv2.imshow(
    "GreenToRed", # имя окна
    img_n # переменная, содержащая изображение
)
cv2.waitKey(4000)
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27: # 27 - код клавиши Esc
        break
cv2.destroyAllWindows()