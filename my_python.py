
import cv2
from zmq import EVENT_CLOSE_FAILED
'''
import numpy
img=cv2.imread("D:\\FFT2.PNG")
cv2.imshow("picture",img)
print(img.shape)
cv2.waitkey(0)
cv2.imwrite("E:\\fft3.PNG",img)

'''
'''

cv2.namedWindow("new",cv2.WINDOW_AUTOSIZE)
cv2.imshow('new',0)
cv2.waitKey(0)
cv2.destroyAllWindows() 
'''

cv2.namedWindow('img',cv2.WINDOW_NORMAL)
img=cv2.imread("D:\\FFT2.PNG")
while True:
 cv2.imshow('img',img)
 key=cv2.waitKey(0)
 if((key & 0xff)==ord('q')):
     print('you key q')
     break
 elif((key & 0xff)==ord('s')):
     print('you key s')
     cv2.imwrite("D:\\FFT2_cp.PNG",img)
 else:
    print('you key other')

cv2.destroyAllWindows()

