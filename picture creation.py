import cv2
import numpy as np
# frame = np.array([[0,0,0],[0,0,0],[0,0,0]])
# # print(frame)
# frame[1,2]=255
# # print(frame)
while True:
    frame1 = np.zeros([240,360,3],dtype= np.uint8)
    frame1[:,:]=[255,255,255]
    frame1[:80,:]=[25,87,255]
    frame1[90:150,150:210]=[128,0,0]
    frame1[160:240,:]=[0,255,0]
    cv2.imshow('flag',frame1)
    if cv2.waitKey(1) & 0xff==ord(' '):
        break