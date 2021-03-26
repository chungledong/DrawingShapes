import cv2 as cv
import numpy as np

BLUE = (255, 0, 0)
p0, p1 = (100, 300), (400, 90)
RED = (0, 0, 255)

def mouse(event, x, y, flags, param):
    global p0, p1

    if event == cv.EVENT_LBUTTONDOWN:
        p0 = (x, y)
        p1 = (x, y)
    elif event == cv.EVENT_MOUSEMOVE and flags == 1:
        p1 = (x, y)
        # vẽ lại hình ảnh trước đó
        img[:] = img0
        cv.line(img, p0, p1, BLUE, 2)
    elif event == cv.EVENT_LBUTTONUP:
        img[:] = img0
        cv.line(img, p0, p1, RED, 5)
        # lưu lại hình ảnh đã vẽ
        img0[:] = img

    cv.imshow("Img", img)

img0 = np.zeros((200, 500, 3), np.uint8)
img = img0.copy()
cv.imshow("Img", img)
# Gọi sự kiện chuột thông qua hàm định nghĩa trên
cv.setMouseCallback("Img",mouse)

cv.waitKey(0)
cv.destroyAllWindows()