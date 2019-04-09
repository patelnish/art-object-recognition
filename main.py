import os
import numpy
import cv2
import matplotlib.pyplot as plt
#print(os.getcwd())
# cv2.__version__


img = cv2.imread('sample_art/moon_sun_piece.png', 1)

# cv2.IMREAD_COLOR - load color image neglect existing transparency 1


plt.imshow(img, cmap='gray', interpolation="bicubic")
