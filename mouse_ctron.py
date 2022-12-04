#setMouseCallback(winname,callback,userdata# )
#callback(event,s,y,flags,userdata)even:事件
import cv2
import numpy as np

#定义一个鼠标回调函数
def mouse_callback(event,x,y,flag,userdata):
    print(event,x,y,flag,userdata)

#调用回调函数，测试一下
#mouse_callback(1,100,100,2,'666')

#创建一个窗口
cv2.namedWindow('mouse',cv2.WINDOW_NORMAL)
cv2.resizeWindow('mouse',640,360)

#设置鼠标回调函数
cv2.setMouseCallback('mouse',mouse_callback,'123')

#显示窗口
img=np.zeros((360,640,3),np.uint8)
while True:
    cv2.imshow('mouse',img)
    key=cv2.waitKey(1)
    if(key & 0xff)==ord('q'):
        break
cv2.destroyAllWindows()   