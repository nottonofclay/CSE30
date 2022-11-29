#
# DO NOT FORGET TO ADD COMMENTS!!!
#
from stack import Stack
from tree import ExpTree

def priority(first_op, second_op):
    if (second_op == None) or (second_op == '('):
        return True
    if (first_op in '^') and (second_op in '+-*/'):
        return True
    if (first_op in '*/') and (second_op in '+-'):
        return True
    return False

def infix_to_postfix(input):
    infix = []
    op = Stack()
    num = []
    postfix = ''
    temp = ''
    while (len(input) != 0):
        if (input[0] in '(+-*/^)'):
            if (len(temp) > 0):
                infix.append(temp)
            infix.append(input[0])
            input = input[1:]
            temp = ''
        else:
            temp += input[0]
            input = input[1:]
    infix.append(temp)
    for i in infix:
        print(f'here: ({postfix}), {i}, ({op.peek()})')
        if (i == ''):
            break
        elif (i[0].isnumeric()):
            postfix += i + ' '
        elif (i == '('):
            op.push(i)
        elif (i == ')'):
            while (True):
                if (op.peek() == '('):
                    op.pop()
                    break
                postfix += op.pop() + ' '
        else:
            if (priority(i, op.peek())):
                op.push(i)
            else:
                postfix += op.pop() + ' '
                op.push(i)
    while (op.peek() != None):
        postfix += op.pop() + ' '
    return postfix
    #         if (i in '+-'):
    #             if (op.peek() == None):
    #                 op.push(i)
    #                 continue
    #             if (op.peek() in '*/^'):
    #                 try:
    #                     postfix += num[-1] + ' ' + num[-2] + ' '
    #                 except:
    #                     if (len(num) > 0):
    #                         postfix += str(num[-1]) + ' '
    #                 num = num[:-2]
    #                 postfix += op.pop() + ' '
    #         if (i in '*/'):
    #             if (op.peek() == None):
    #                 op.push(i)
    #                 continue
    #             if (op.peek() in '^'):
    #                 try:
    #                     postfix += num[-1] + ' ' + num[-2] + ' '
    #                 except:
    #                     if (len(num) > 0):
    #                         postfix += str(num[-1]) + ' '
    #                 num = num[:-2]
    #                 postfix += op.pop() + ' '
    #         op.push(i)
    # while (len(num) > 0) and (op.peek() != None):
    #     postfix += (str(num[-1]) + ' ')
    #     num = num[:-1]
    #     postfix += op.pop() + ' '
    # while (op.peek() != None):

    #     postfix += op.pop() + ' '


def calculate(infix):

    input = infix_to_postfix(infix)
    tree = ExpTree.make_tree(input.split())
    return ExpTree.evaluate(tree)

# a driver to test calculate module
if __name__ == '__main__':
    print('Welcome to Calculator Program!')
    while(True):
        expression = input('Please enter your expression here. To quit enter \'quit\' or \'q\':')
