import cv2
import numpy as np

img = np.zeros((480,640,3),np.uint8)

#图形分割,将img图像的三个通道都分割出去，分别是
#B,G,R,

b,g,r =cv2.split(img)

b[10:100,10:100]=255
g[100:200,100:200]=255

cv2.imshow('img',img)
cv2.imshow('b',b)
cv2.imshow('g',g)
cv2.imshow('r',r)

#图像合并
img2=cv2.merge((b,g,r))
cv2.imshow('img2',img2)




cv2.waitKey(0)

