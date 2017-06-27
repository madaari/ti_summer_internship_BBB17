#!/bin/usr/env python2.7
import cv2

def caminit(cap):
    cap.set(3, 100)
    cap.set(4, 280)
    print(cap.get(3)) # Width of pic
    print(cap.get(4)) # Height of pic




print(cv2.__version__)

cap = cv2.VideoCapture(2)
caminit(cap)
print("Press any key to skip")
while (True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray[0:400,300:360])
    if  cv2.waitKey(1) != -1:
        break

cap.release()
cv2.destroyAllWindows()
