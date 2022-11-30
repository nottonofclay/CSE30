def hash(astring, size):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[ pos])
    return sum % size

test2 = ['cat', 'dog', 'horse', 'cow', 'bird', 'turtle', 'rabbit']
print(test2)
hashes = [hash(x, len(test2)) for x in test2]
print(hashes)