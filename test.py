import os
import cv2
import numpy as np
os.chdir('C:/Users/tonof/Onedrive/Documents/Code/CSE30/PA3_Cryptography')

image = cv2.imread('redbox.jpg')

binary = '011010000110010101101100011011000110111100100011'
count = 0


for pos, i in np.ndenumerate(image):
    value = image[pos[0]][pos[1]][pos[2]]
    if (binary[count] == '0') and (value % 2 != 0):
        if (value == 255):
            image[pos[0]][pos[1]][pos[2]] -= 1
        else:
            image[pos[0]][pos[1]][pos[2]] += 1
    elif (binary[count] == '1') and (value % 2 == 0):
        image[pos[0]][pos[1]][pos[2]] += 1
    count += 1
    if (count >= len(binary)):
        break

print(image.reshape(image.size))

# print(np.reshape(3,10,10))
# print(image)