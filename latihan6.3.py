# Akbar Kamaludin
# 1217070009
import cv2
import  numpy as np
image = cv2.imread("aboy.jpg")
# flipping horizontal
flip_hor=cv2.flip(image,1)
# flipping vertical
flip_ver=cv2.flip(image,0)
# flipping vertical-horizontal
flip_verhor=cv2.flip(image,-1)
cv2.imshow('Citra Original', image)
cv2.imshow('Citra flip horizontal',flip_hor)
cv2.imshow("citra flip vertikal",flip_ver)
cv2.imshow('Citra flip vertikal-horizontal',flip_verhor)
cv2.waitKey(0)