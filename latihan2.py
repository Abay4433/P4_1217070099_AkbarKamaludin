# Akbar Kamaludin
# 1217070009
import cv2
import numpy as np

image = cv2.imread('aboy.jpg')

# maxiimum pixel
max_pixel = 255
citra_negatif = max_pixel - image

cv2.imshow('Original', image)
cv2.imshow('Negatif', citra_negatif)
cv2.waitKey(0)
cv2.destroyAllWindows()