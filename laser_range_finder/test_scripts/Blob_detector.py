#!/bin/usr/env Python2.7
import cv2
import numpy as np


def caminit(cap):
    print(cap.get(3)) # Width of pic
    print(cap.get(4)) # Height of pic
    cap.set(3,640)
    cap.set(4,720)

def invert_color(frame):
    return 255-frame

def getBlobDetector():
    params = cv2.SimpleBlobDetector_Params()
    params.filterByArea = True
    params.minArea = 0.1
    params.maxArea = 350
    params.filterByCircularity = True
    params.minCircularity = 0.9
    params.filterByConvexity = True
    params.minConvexity = 0.87
    params.filterByInertia = True
    params.minInertiaRatio = 0.01
    return cv2.SimpleBlobDetector(params)

print(cv2.__version__)

cap = cv2.VideoCapture(2)
print(cap.isOpened())
detector = getBlobDetector()
caminit(cap)
print("Press any key to skip")
prev_frame = 0
while (cap.isOpened()):
    ret, frame = cap.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    gray = frame
    gray = invert_color(gray)
    sub_frame = gray
    keypoints = detector.detect(sub_frame)
    if len(keypoints) != 0:
        im_with_keypoints = cv2.drawKeypoints(sub_frame, keypoints, np.array([]), (0, 0, 255),
                                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        cv2.imshow('frame', im_with_keypoints)
        if cv2.waitKey(1) != -1:
            break
    else:
        pass
    prev_frame = gray
cap.release()
cv2.destroyAllWindows()
