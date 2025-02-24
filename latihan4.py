# Akbar Kamaludin
# 1217070009
import cv2
import numpy as np

image=cv2.imread('aboy.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
MatriksSatu = np.ones(image.shape[:2],image.dtype)*100

# Operasi penjumlahan
citraPenjumlahan= cv2.add(gray, MatriksSatu)
cv2.imshow('Citra', gray)
cv2.imshow('Citra Penjumlahan', citraPenjumlahan)
cv2.waitKey()

