"""
Напишите свою реализацию операций замыкания и размыкания 
для нескольких итераций. Каждую операцию оформите в виде отдельной 
функции (допустимый вариант - одна функция для двух операций, где тип 
операции задается через аргумент). Функция должна принимать исходное 
изображение, ядро и другие аргументы при необходимости. В вашей 
реализации замыкания и размыкания можно (нужно) использовать функции 
эрозии и наращивания, реализованные в OpenCV.    
На данном изображении добейтесь полной заливки кругов с 
использованием первой функции. С помощью операции размыкания удалите 
всё содержимое кругов на исходном изображении, затем сохраните его на 
компьютер. Сравните результат работы ваших функций с реализацией замыкания 
и размыкания в OpenCV.  Для сравнения результата можно использовать 
попиксельно сравнение изображений.
"""
import cv2
import numpy as np


def custom_morphology(image, kernel, operation, iterations=1):
    result = image.copy()
    for _ in range(iterations):
        if operation == 'close':
            result = cv2.dilate(result, kernel)
            result = cv2.erode(result, kernel)
        elif operation == 'open':
            result = cv2.erode(result, kernel)
            result = cv2.dilate(result, kernel)
    return result

image_path = r"D:\pythonprograms\techvision\techvision_etu_2025\src\lab2\images\1.jpg"
image = cv2.imread(image_path)

kernel = np.ones((5, 5), np.uint8)

# Пользовательское замыкание (заливка кругов)
custom_close = custom_morphology(image, kernel, 'close', iterations=3)
cv2.imshow("Custom Closing", custom_close)
cv2.waitKey(2000)

# Пользовательское размыкание (удаление содержимого кругов)
custom_open = custom_morphology(image, kernel, 'open', iterations=3)
cv2.imshow("Custom Opening", custom_open)
cv2.waitKey(2000)

# Сохраняем результат
cv2.imwrite(r"D:\pythonprograms\techvision\techvision_etu_2025\src\lab2\images\custom_result.jpg", custom_open)

# Сравнение с OpenCV
opencv_close = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel, iterations=1)
opencv_open = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel, iterations=1)

cv2.imshow("OpenCV Opening", opencv_open)
cv2.imshow("OpenCV Closing", opencv_close)

opencv_open_path = r"D:\pythonprograms\techvision\techvision_etu_2025\src\lab2\images\opencv_open.jpg"
cv2.imwrite(opencv_open_path, opencv_open)

opencv_close_path = r"D:\pythonprograms\techvision\techvision_etu_2025\src\lab2\images\opencv_close.jpg"
cv2.imwrite(opencv_close_path, opencv_close)

custom_close_path = r"D:\pythonprograms\techvision\techvision_etu_2025\src\lab2\images\custom_close.jpg"
cv2.imwrite(custom_close_path, custom_close)

custom_open_path = r"D:\pythonprograms\techvision\techvision_etu_2025\src\lab2\images\custom_open.jpg"
cv2.imwrite(custom_open_path, custom_open)

# Попиксельное сравнение
diff_close = cv2.absdiff(custom_close, opencv_close)
diff_open = cv2.absdiff(custom_open, opencv_open)

print(f"Различия в замыкании: {np.sum(diff_close > 0)} пикселей")
print(f"Различия в размыкании: {np.sum(diff_open > 0)} пикселей")

cv2.waitKey(0)
cv2.destroyAllWindows()