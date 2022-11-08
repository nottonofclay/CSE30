# codecs
import numpy as np

class Codec():

    def __init__(self):
        self.name = 'binary'
        self.delimiter = '#'

    # convert text or numbers into binary form
    def encode(self, text):
        if type(text) == str:
            return ''.join([format(ord(i), "08b") for i in text])
        else:
            print('Format error')

    # convert binary data into text
    def decode(self, data):
        binary = []
        for i in range(0,len(data),8):
            byte = data[i: i+8]
            if byte == self.encode(self.delimiter):
                break
            binary.append(byte)
        text = ''
        for byte in binary:
            text += chr(int(byte,2))
        return text

class CaesarCypher(Codec):

    def __init__(self, shift=3):
        self.name = 'caesar'
        self.delimiter = '#'
        self.shift = shift
        self.chars = 256      # total number of characters

    # convert text into binary form
    # your code should be similar to the corresponding code used for Codec
    def encode(self, text):
        if type(text) == str:
            return ''.join([format((ord(i) + self.shift)%256, "08b") for i in text])
        else:
            print('Format error')# your code goes here

    # convert binary data into text
    # your code should be similar to the corresponding code used for Codec
    def decode(self, data):
        binary = []
        for i in range(0,len(data),8):
            byte = data[i: i+8]
            if byte == self.encode(self.delimiter):
                break
            binary.append(byte)
        text = ''
        for byte in binary:
            try:
                text += chr(int(byte,2) - self.shift)
            except:
                text += chr(255 + int(byte,2) - self.shift)
        return text

# a helper class used for class HuffmanCodes that implements a Huffman tree
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.left = left
        self.right = right
        self.freq = freq
        self.symbol = symbol
        self.code = ''

class HuffmanCodes(Codec):

    def __init__(self):
        self.nodes = None
        self.data = {}
        self.name = 'huffman'
        self.delimiter = '#'

    # make a Huffman Tree
    def make_tree(self, data):
        # make nodes
        nodes = []
        key = {}
        for char, freq in data.items():
            nodes.append(Node(freq, char))

        # assemble the nodes into a tree
        while len(nodes) > 1:
            # sort the current nodes by frequency
            nodes = sorted(nodes, key=lambda x: x.freq)

            # pick two nodes with the lowest frequencies
            left = nodes[0]
            right = nodes[1]

            # assign codes
            left.code = '0'
            right.code = '1'

            # combine the nodes into a tree
            root = Node(left.freq+right.freq, left.symbol+right.symbol,
                        left, right)

            # remove the two nodes and add their parent to the list of nodes
            nodes.remove(left)
            nodes.remove(right)
            nodes.append(root)
        self.nodes = nodes[0]
        return nodes[0]

    def make_key(self, node, val):
        next_val = val + node.code
        if(node.left):
            self.make_key(node.left, next_val)
        if(node.right):
            self.make_key(node.right, next_val)
        if(not node.left and not node.right):
            self.data[node.symbol] = next_val

    # traverse a Huffman tree
    def traverse_tree(self, node, val):
        current_node = node
        output = ''
        for i in val:
            if (val[0] == '0'):
                try:
                    current_node.right.symbol
                    current_node = current_node.left
                    val = val[1:]
                except:
                    if (current_node.symbol == '#'):
                        break
                    output += current_node.symbol
                    current_node = node
            if (val[0] == '1'):
                try:
                    current_node.left.symbol
                    current_node = current_node.right
                    val = val[1:]
                except:
                    if (current_node.symbol == '#'):
                        break
                    output += current_node.symbol
                    current_node = node
        return output

    # convert text into binary form
    def encode(self, text):
        data = ''
        freq = {}
        for i in text:
            try:
                freq[i] += 1
            except:
                freq[i] = 1
        self.make_key(self.make_tree(freq), '')
        for i in text:
            data += self.data[i]
        return data


    # convert binary data into text
    def decode(self, data):
        # output = ''
        # key = ''
        # for i in range(len(data)):
        #     key += data[i]
        #     if (key in list(self.data.values())):
        #         word = [i for i in self.data.keys() if self.data[i] == key]
        #         if (word[0] == '#'):
        #             return output
        #         output += word[0]
        #         key = ''
        return self.traverse_tree(self.nodes, data)


if __name__ == '__main__':
    text = 'helllo my name is raj'
    cc = HuffmanCodes()
    binary = cc.encode(text + cc.delimiter)
    print('Binary:', binary)
    data = cc.decode(binary)
    print('Text:', data)