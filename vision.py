from __future__ import barry_as_FLUFL
from tkinter import Frame
import cv2 as cv
from cv2 import imshow;


# READ IMAGES
# img = cv.imread('assets/imgs/img2.jpeg')
# cv,imshow("visionary", img)
# cv.waitKey(0)

# READ VIDOES
vid = cv.VideoCapture('assets/vids/2021-08-04 17-38-29.mp4')

while True:
    isTrue, frame = vid.read()
    cv.imshow('visionary', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

vid.release()
vid.destoryAllWindos()