# Akbar Kamaludin
# 1217070009

import cv2
import numpy as np
image = cv2.imread('aboy.jpg')
b,g,r = cv2.split(image)
# Buat matriks seukuran dengan citra
matriks0 = np.zeros(image.shape[:2],image.dtype)
m = matriks0
# merge matriks dengan matriks channel merah
merah = cv2.merge([m,m,r])
cv2.imshow("Citra red channel", merah)
cv2.waitKey(0)
