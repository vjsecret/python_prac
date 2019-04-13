import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Desert.jpg',1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([img],[0],None,[256],[0,256])

plt.plot(hist)
plt.show()