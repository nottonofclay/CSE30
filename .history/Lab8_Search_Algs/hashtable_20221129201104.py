class Hashtable():
    def __init__(self):
        self.table = [[], [], [], [], [], [], [], [], [], []]

    def get(key):
        pass

    def get_size():
        pass

    def add(self, key, value):
        pass

    def remove(key):
        pass

    def is_empty(self):
        for i in self.table:
            if len(i) < 0:
                return False
        return True

data = ['goat', 'pig', 'chicken', 'dog', 'lion', 'tiger', 'cow', 'cat']

# make a hash table with key-value pairs: 'goat': 0, 'pig': 1, 'chicken': 2, etc.
h = Hashtable()
print(h.is_empty())
for i in range(len(data)):
    h.add(data[i], i)       # the key is data[i], the value is i

# print the hash table items
for key in data:
    print(h.get(key))

# test the method get() and if items in the hash table are correct
for i in range(len(data)):
    assert h.get(data[i]) == i

# test the method get_size()
n = h.get_size()
assert n == 8

# test the method remove() and is_empty()
for i in data:
    h.remove(i)
print(h.is_empty())
assert h.is_empty()
