from gc import callbacks
from operator import index
import cv2
def callback():
    pass
#创建一个窗口
cv2.namedWindow('color',cv2.WINDOW_NORMAL)

#读取一个图片
img=cv2.imread('D:\open_cv.jpg')
#创建一个数组
colorspaces=[cv2.COLOR_BGR2RGBA,cv2.COLOR_BGR2BGRA,
             cv2.COLOR_BGR2GRAY,cv2.COLOR_BGR2HSV,
             cv2.COLOR_BGR2YUV]
#创建一个Trackbar,名称是curcolor,依附在color窗口
cv2.createTrackbar('curcolor','color',0,4,callback)

while True:
    #获取color窗口的curcolor的值
    index = cv2.getTrackbarPos('curcolor','color')

    cvt_img=cv2.cvtColor(img,colorspaces[index])
    cv2.imshow('color',cvt_img)

    key= cv2.waitKey(10)
    if key & 0xff == ord('q'):
        break
cv2.destroyAllWindows()   

