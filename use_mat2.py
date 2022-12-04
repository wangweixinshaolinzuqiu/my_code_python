import cv2
import numpy as np

img = cv2.imread('d:\\open_cv.jpg')

#shape 属性，包括，高度，长度，和通道数
print(img.shape)

# h * l* chanl
print(img.size)

#图像每个元素的位深
print(img.dtype)
