# steganography
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import ceil
from codec import Codec, CaesarCypher, HuffmanCodes
import os


class Steganography():

    def __init__(self):
        self.text = ''
        self.binary = ''
        self.delimiter = '#'
        self.codec = None

    def encode(self, filein, fileout, message, codec):
        image = cv2.imread(filein)

        # calculate available bytes
        max_bytes = image.shape[0] * image.shape[1] * 3 // 8
        print("Maximum bytes available:", max_bytes)

        # convert into binary
        if codec == 'binary':
            self.codec = Codec()
        elif codec == 'caesar':
            while True:
                shift = input('Please enter a shift size: ')
                try:
                    shift = int(shift)
                    break
                except:
                    print('Please enter an integer!')
            self.codec = CaesarCypher(shift=shift)
        elif codec == 'huffman':
            self.codec = HuffmanCodes()
        binary = self.codec.encode(message + self.delimiter)

        # check if possible to encode the message
        num_bytes = ceil(len(binary)//8) + 1
        if  num_bytes > max_bytes:
            print("Error: Insufficient bytes!")
        else:
            print("Bytes to encode:", num_bytes)
            self.text = message
            self.binary = binary
            count = 0
            for pos, i in np.ndenumerate(image):
                value = image[pos[0]][pos[1]][pos[2]]
                if (self.binary[count] == '0') and (value % 2 != 0):
                    if (value == 255):
                        image[pos[0]][pos[1]][pos[2]] -= 1
                    else:
                        image[pos[0]][pos[1]][pos[2]] += 1
                elif (self.binary[count] == '1') and (value % 2 == 0):
                    image[pos[0]][pos[1]][pos[2]] += 1
                count += 1
                if (count >= len(binary)):
                    break
            cv2.imwrite(fileout, image)

    def decode(self, filein, codec):
        image = cv2.imread(filein)
        flag = True

        # convert into text
        if codec == 'binary':
            self.codec = Codec()
        elif codec == 'caesar':
            while True:
                shift = input('Please enter a shift size: ')
                try:
                    shift = int(shift)
                    break
                except:
                    print('Please enter an integer!')
            self.codec = CaesarCypher(shift=shift)
        elif codec == 'huffman':
            self.codec = HuffmanCodes()
        if flag:
            binary_data = ''
            for i in np.nditer(image):
                binary_data += str(i % 2)
            self.text = self.codec.decode(binary_data)
        print(self.text)

    def print(self):
        if self.text == '':
            print("The message is not set.")
        else:
            print("Text message:", self.text)
            print("Binary message:", self.binary)

    def show(self, filename):
        print(mpimg.imread(filename))
        plt.imshow(mpimg.imread(filename))
        plt.show()
