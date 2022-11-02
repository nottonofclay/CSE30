import numpy as np



output = ''
text = 'hello'
output = output.join([format(ord(i), "08b") for i in text])
# print(output)


# print(format(ord('A') + 3))

byte = format(ord('z'), "08b")

print(byte)

print(chr(int(byte,2)))

