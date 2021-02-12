import tkinter as tk
from tkinter import *
import cv2 as cv
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="video path")
args = vars(ap.parse_args())
