""" Topic 5. Working with Images"""

import numpy as np
import cv2
import matplotlib.pyplot as plt


#read an image
img = cv2.imread('D:\\NUMPY\\numpy_tricks\\cv2_image.jpg')
print(img)                            #return an array


#shape --> show array shape
print(img.shape)                      #((188, 269, 3)


#show image
plt.imshow(img)
plt.show()


#flip
plt.imshow(np.flip(img))
plt.show()


#clip
print(img.min())                # 0 
print(img.max())                #255


#clip
print(plt.imshow(np.clip(img, 0, 100)))         #brightness reduced
plt.show()                   


#negative
print(plt.imshow(255 - img))         
plt.show()


#trim
print(plt.imshow(img[100:900, 50:900, :]))       #used in croping purposes
plt.show()


#plot histogram
plt.hist(img.flatten(), bins=255)
plt.show()