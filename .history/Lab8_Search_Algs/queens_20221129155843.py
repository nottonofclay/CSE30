# make a generator
def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]

def find_solutions(size):
    data = range(1,size)
    for i in data:
        print(all_perms(data))

if __name__ == '__main__':
    find_solutions(4)