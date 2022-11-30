test = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# simple hashing based on the modulo operation
index = [x % 9 for x in test]

# mid-square hash function
k = 0
for item in test:
    item = str(item*item)
    s = item
    #print(s)
    if len(item) > 1:
        #print(len(item)//2, len(item)//2 + 1)
        s = item[len(item)//2-1] + item[len(item)//2]
    index[ k] = int(s) % len(test)
    k += 1
print(index)