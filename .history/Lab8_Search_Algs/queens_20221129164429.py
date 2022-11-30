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
    solutions = []
    for perm in all_perms(data):
        solution = True
        for i in range(len(perm)):
            for j in range(i + 1, len(perm)):
                if (abs(i-j) == abs(perm[i]-perm[j])):
                    solution = False
        if (solution):
            solutions.append(perm)
    return solutions


if __name__ == '__main__':
    while(True):
        size = input('Enter a number of queens:\n')
        if (size.isdigit()):
            solutions = find_solutions(int(size))
            print(f'The {size}-queens puzzle has {len(solutions)} solutions:')
            for i in solutions:
                print(i)
            break
        else:
            print('Please enter a number')
