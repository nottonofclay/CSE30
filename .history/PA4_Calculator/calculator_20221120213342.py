#
# DO NOT FORGET TO ADD COMMENTS!!!
#
from stack import Stack
from tree import ExpTree

def infix_to_postfix(infix):
    op = Stack()
    num = ''
    postfix = ''
    for i in infix:
        # print(f'here is the stakc: {op.peek()}')
        # print(f'here is the num: {num}')
        # print(f'here is the postfix: {postfix}')
        if (i.isdigit()) or (i == '.'):
            num += i
        elif (i == '('):
            op.push(i)
        elif (i == ')'):
            postfix += num[0] + ' ' + num[1] + ' '
            num = num[2:]
            while (True):

                if (op.peek() == '('):
                    op.pop()
                    break
                postfix += op.pop() + ' '
        else:
            # if (i in '*/'):
            #     if (op.peek() in '+-'):
            #         postfix += op.pop() + ' '
            if (i in '+-'):
                if (op.peek() == None):
                    op.push(i)
                    continue
                if (op.peek() in '*/'):
                    postfix += str(num[0]) + ' '
                    postfix += str(num[1]) + ' '
                    num = num[2:]
                    postfix += op.pop() + ' '
            op.push(i)
        print(f'here is the postfix: {op.array}')
    while (num != ''):
        postfix += (str(num[0]) + ' ')
        num = num[1:]
    while (op.peek() != None):
        postfix += op.pop() + ' '
    return postfix

def calculate(infix):
    input = infix_to_postfix(infix)
    tree = ExpTree.make_tree(input.split())
    return ExpTree.evaluate(tree)

# a driver to test calculate module
if __name__ == '__main__':

    # test infix_to_postfix function
    print('\nhere is the final postfix: ', end='')
    print(infix_to_postfix('(5+2)*3+4'))
    # print(calculate('5+2*3'))
    # assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'
    # assert infix_to_postfix('5+2*3') == '5 2 3 * +'

    # # test calculate function
    # assert calculate('(5+2)*3') == 21.0
    # assert calculate('5+2*3') == 11.0