#
# DO NOT FORGET TO ADD COMMENTS!!!
#
from stack import Stack
from tree import ExpTree

def infix_to_postfix(input):
    infix = []
    op = Stack()
    num = []
    postfix = ''
    temp = ''
    while (len(input) != 0):
        if (input[0] in '(+-*/)'):
            if (len(temp) > 0):
                infix.append(temp)
            infix.append(input[0])
            input = input[1:]
            temp = ''
        else:
            temp += input[0]
            input = input[1:]
    infix.append(temp)
    print(infix)
    for i in infix:
        if (i.isnumeric()):
            num.append(i)
        elif (i == '('):
            op.push(i)
        elif (i == ')'):
            postfix += num[-1] + ' ' # + num[-1] + ' '
            num = num[:-2]
            while (True):
                if (op.peek() == '('):
                    op.pop()
                    break
                postfix += op.pop() + ' '
        else:
            if (i in '+-'):
                if (op.peek() == None):
                    op.push(i)
                    continue
                if (op.peek() in '*/'):
                    postfix += str(num[-1]) + ' ' # + num[-1] + ' '
                    num = num[:-2]
                    postfix += op.pop() + ' '
            op.push(i)
    while (len(num) > 0):
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

    print('\nhere is the final postfix: ', end='')
    print(infix_to_postfix('(1+2)*((2-0)+1)+6'))
    # print(calculate('(5+2)*3'))
    # assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'
    # assert infix_to_postfix('5+2*3') == '5 2 3 * +'

    # # test calculate function
    # assert calculate('(5+2)*3') == 21.0
    # assert calculate('5+2*3') == 11.0