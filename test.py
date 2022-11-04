import os
import cv2
os.chdir('C:/Users/tonof/OneDrive/Documents/Code/CSE30/PA3_Cryptography')

image = cv2.imread('redbox.jpg')

print(type(image))

for i in range(len(image)):
    for j in range(len(image[i])):
        print(f'{i}.{j}: {image[i][j]}')

