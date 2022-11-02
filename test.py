import numpy as np



output = ''
text = 'hello'
output = output.join([format(ord(i), "08b") for i in text])
# print(output)


# print(format(ord('A') + 3))

print(ord(None))

byte = format(ord('a'), "08b")

print(byte)

print(chr((int(byte,2) - 2)%256))

print(-2 % 256)

