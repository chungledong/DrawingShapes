import cv2 as cv
import numpy as np
# Chọn độ dày của đường thằng bẳng phương pháp động

RED = (0, 0, 255)
p0, p1 = (100, 30), (400, 90)
# Định nghĩa hàm độ dày của đường thăẳng
def trackbar(x):
    x = max(1, x)
    img[:] = 0
    cv.line(img, p0, p1, RED, x)
    cv.imshow("Img", img)

img = np.zeros((200, 500, 3), np.uint8)

cv.line(img, p0, p1, RED, 2)
cv.imshow("Img", img)
cv.createTrackbar("thickness", "Img", 2, 80, trackbar)

cv.waitKey(0)
cv.destroyAllWindows()
