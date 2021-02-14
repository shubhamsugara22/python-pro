import tkinter as tk
from tkinter import *
import cv2
from cv2 import *
import argparse
from argparse import *

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="video path")
args = vars(ap.parse_args())

camVideo = cv2.VideoCapture(args["video"])

while True:
    (grabbed, frame) = camVideo.read()
    status = "No target in sight"

    if not grabbed:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # grayscale
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)  # blur
    edged = cv2.Canny(blurred, 50, 150)  # canny edge detection

    (cnts, _) = cv2.findContours(edged.copy(),
                                 cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in cnts:
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)

if len(approx) == 5:
    cv2.drawContours(frame, [approx], -1, (0, 0, 255), 4)
    status = "Target(s) in sight!"

    cv2.putText(frame, status, (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        break

camVideo.release()
cv2.destroyAllWindows()
