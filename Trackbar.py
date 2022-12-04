#CV_EXPORTS int createTrackbar(const string& trackbarname, 轨迹条名称
# const string& winname,int* value,      winname：依附在哪个窗口， value:滑块位置
# int count,  滑块位置的最大值
# TrackbarCallback onChange = 0,void* userdata = 0);回调函数指针，用户传给回调函数的参数

#int getTrackbarPos(const String& trackbarname,轨迹条名称
#  const String& winname)                      轨迹条所在的窗口名称

import traceback
import cv2
import numpy as np

def callback():
    pass
cv2.namedWindow('trackbar',cv2.WINDOW_NORMAL)


cv2.createTrackbar('R','trackbar',0,255,callback)
cv2.createTrackbar('G','trackbar',0,255,callback)
cv2.createTrackbar('B','trackbar',0,255,callback)

img=np.zeros((480,460,3),np.uint8)

while True :
     cv2.imshow('trackbar',img)
     #获取Trackbar的值
     GRB_R=cv2.getTrackbarPos('R','trackbar')
     GRB_G=cv2.getTrackbarPos('G','trackbar')
     GRB_B=cv2.getTrackbarPos('B','trackbar')
     #对img图片所有的像素进行操作
     img[:]=[GRB_B,GRB_G,GRB_R]
     key=cv2.waitKey(10)
     if (key & 0xff)==ord('q'):
         break
cv2.destroyAllWindows()
