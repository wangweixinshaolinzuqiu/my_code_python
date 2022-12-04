import cv2
#创建窗口
cv2.namedWindow('video',cv2.WINDOW_NORMAL)
cv2.resizeWindow('video',640,480)
#获取视频设备0,或者从视频文件中获得视频帧
# cap=cv2.VideoCapture(0)
cap=cv2.VideoCapture('D:\\opcv_cs.mp4')

while True:
    #从摄像头读视频帧
    ret,frame = cap.read()
    #将视频帧在窗口显示
    cv2.imshow('video',frame)
    key=cv2.waitKey(33)
    if(key & 0xff == ord('q')):
      break
cap.release()
cv2.destroyAllWindows()
