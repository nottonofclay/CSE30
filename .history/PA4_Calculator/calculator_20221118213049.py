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
        if (i.isdigit()) or (i == '.'):
            num += i
        elif (i == '('):
            op.push(i)
        elif (i == ')'):
            while (True):
                if (op.peek() == '('):
                    op.pop()
                    break
                postfix += op.pop()
        else:
            if (i in '+-'):
                if (op.peek() in '*/'):
                    postfix += op.pop()
            op.push(i)



def calculate(infix):
    tree = ExpTree.make_tree(infix.split())
    return ExpTree.evaluate()

# a driver to test calculate module
if __name__ == '__main__':

    # test infix_to_postfix function
    print(infix_to_postfix('5+2*3'))
    assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'
    assert infix_to_postfix('5+2*3') == '5 2 3 * +'

    # test calculate function
    assert calculate('(5+2)*3') == 21.0
    assert calculate('5+2*3') == 11.0