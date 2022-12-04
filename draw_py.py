#from gettext import npgettext
import cv2
import numpy as np

img =np.zeros((480,640,3),np.uint8)

#画直线
cv2.line(img,(10,10),(300,300),(0,0,255),1,16)
cv2.line(img,(50,10),(350,300),(0,0,255),1,16)

#cv2.imshow('draw',img)
#画矩形             对角坐标           颜色    线条宽度，取负值填充
cv2.rectangle(img,(10,10),(100,100),(0,225,0),   1)

#画圆                               线条宽度，取负值填充
cv2.circle(img,(300,300),100,(255,0,0),10)

#画椭圆,0度从右边开始，顺时针旋转       角度  右边开始
cv2.ellipse(img,(300,300),(100,50),  90   , 0  ,360,   (0,0,255),1)

#画多边形  数据类型必须时32 位的np.int32
pts=np.array([(300,10),(150,100),(450,100)],np.int32)
cv2.polylines(img,[pts],True,(0,0,255),10)
#多边形颜色填充
cv2.fillPoly(img,[pts],(255,0,0))

#绘制文本       字体cv2.FONT_HERSHEY_PLAIN等（0-7）   字号    颜色
cv2.putText(img,"hellow world!",(10,400),    0   ,   2    ,(0,255,0))

cv2.imshow('draw',img)
cv2.waitKey(0)