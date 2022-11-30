# make a generator
def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]

def find_solutions(size):
    data = list(range(1,size+1))
    for perm in all_perms(data):
        solution = True
        for i in range(len(perm)):
            for j in range(i + 1, len(perm)):
                if (abs(i-j) == abs(perm[i]-perm[j])):
                    solution = False
        if (solution):
            print(perm)


if __name__ == '__main__':
    find_solutions(8)