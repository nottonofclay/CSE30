# Clayton Lau
# 21 November, 2022
# Creates stack object

class Stack:

    def __init__(self):
        self.array = []

    def isEmpty(self):
        if (len(self.array) == 0):
            return True
        return False

    def push(self, item):
        self.array.append(item)

    def pop(self):
        if (self.isEmpty()):
            return None
        return self.array.pop()

    def peek(self):
        if (self.isEmpty()):
            return None
        return self.array[-1]

    def size(self):
        return len(self.array)

# a driver program for class Stack

if __name__ == '__main__':

    data_in = ['hello', 'how', 'are', 'you']
    s = Stack()
    for i in data_in:
        s.push(i)

    assert s.size() == len(data_in)
    assert s.peek() == data_in[-1]

    data_out = []
    while not s.isEmpty():
        data_out.append(s.pop())

    assert data_out == data_in[::-1]
    assert s.size() == 0
    assert s.peek() == None
