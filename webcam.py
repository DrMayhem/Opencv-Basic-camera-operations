from tracemalloc import Frame
from turtle import width
import cv2 as cv
img = cv.imread("scenery.jpg",)
# width , height = 340,200
# img2 = cv.resize(img, (width, height))
# cv.imshow('Cars',img)
# cv.waitKey(0)
cap = cv.VideoCapture(0,cv.CAP_DSHOW)
# cap.set(cv.CAP_PROP_FRAME_WIDTH,width)
# cap.set(cv.CAP_PROP_FRAME_HEIGHT,height)
# cap.set(cv.CAP_PROP_FPS, 100)
# cap.set(cv.CAP_PROP_FOURCC,cv.VideoWriter_fourcc(*'MJPG'))
while(True):
    ignore, frame = cap.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cv.imshow('my WEBcam',  frame)
    cv.moveWindow('my WEBcam',0,0)
    cv.imshow('my gray pic',gray)
    cv.moveWindow('my gray pic',640,0)
    
    if cv.waitKey(1) & 0xFF == ord(' '):
        break
cap.release()    
cv.destroyAllWindows()     