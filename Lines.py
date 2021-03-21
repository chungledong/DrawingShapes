import cv2 as cv
import numpy as np

#Using Numpy
# 1. Chúng ta tạo một mảng 3D mà các phần tử trong mạng =0

img = np.zeros((100,600, 3), np.uint8)
# Define Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

RED = (0, 0, 255)
YELLOW = (0, 255, 255)
BLUE = (255, 0, 0)

CYAN = (255, 255, 0)
MEGENTA = (255, 0,255)
GREEN = (0, 255, 0)

#. 1 Vẽ đường thằng
cv.line(img, (10 ,10), (300, 90), MEGENTA, 2)
cv.line(img, (300, 90), (500, 10), YELLOW, 5)
print(img.shape)
cv.imshow("RGB", img)

cv.waitKey(0)
cv.destroyAllWindows()