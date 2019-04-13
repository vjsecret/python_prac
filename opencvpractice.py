import cv2
from matplotlib import pyplot as plt
#import matplotlib.pyplot as plt

im = cv2.imread('Desert.jpg',1)
im_rgb=cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
plt.imshow(im_rgb)
plt.show()
