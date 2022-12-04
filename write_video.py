import cv2
#创建多媒体文件
fourcc=cv2.VideoWriter_fourcc(*'MJPG')
vw=cv2.VideoWriter('D:\\opencv.mp4',fourcc,25,(640,480))
#创建窗口
cv2.namedWindow('video',cv2.WINDOW_NORMAL)
cv2.resizeWindow('video',640,480)
#获取视频设备0,或者从视频文件中获得视频帧
cap=cv2.VideoCapture(0)
#cap=cv2.VideoCapture('D:\\opcv_cs.mp4')

while cap.isOpened():
    #从摄像头读视频帧
    ret,frame = cap.read()
    if ret==True:
    #将视频帧在窗口显示
     cv2.imshow('video',frame)
    #写数据到多媒体
     vw.write(frame)
     key=cv2.waitKey(1)
    if(key & 0xff == ord('q')):
      break
cap.release()
#释放资源
vw.release()
cv2.destroyAllWindows()