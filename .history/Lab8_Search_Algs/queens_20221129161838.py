import math

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
        print(f'\n\ni j i j for {perm}')
        for i in range(len(perm)):
            for j in range(i + 1, len(perm)):
                print(i, j, perm[i], perm[j])
                if (math.abs(i-j) == math.abs(perm[i]-perm[j])):
                    break


if __name__ == '__main__':
    find_solutions(4)