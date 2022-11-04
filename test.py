import os
import cv2
import numpy as np
os.chdir('C:/Users/tonof/Documents/Code/CSE30/PA3_Cryptography')

image = cv2.imread('redbox.jpg')

binary = '01110101'


for position, i in np.ndenumerate(image):
    value = image[position[0]][position[1]][position[2]]
    if (value % 2 == 0):
        image[position[0]][position[1]][position[2]]


print(binary)
# print(image)