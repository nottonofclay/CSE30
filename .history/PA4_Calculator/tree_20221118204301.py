#
# DO NOT FORGET TO ADD COMMENTS
#

from stack import Stack

class BinaryTree:
    def __init__(self,rootObj=None):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            t.rightChild = self.rightChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            t.leftChild = self.leftChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def getRootVal(self):
        return self.key

    def setRootVal(self, obj):
        self.key = obj

    def __str__(self):
        s = f"{self.key}"
        s += '('
        if self.leftChild != None:
            s += str(self.leftChild)
        s += ')('
        if self.rightChild != None:
            s += str(self.rightChild)
        s += ')'
        return s

class ExpTree(BinaryTree):

    def make_tree(postfix):
        s = Stack()
        for i in range(len(postfix)):
            if (postfix[i].isdigit()):
                s.push(ExpTree(postfix[i]))
            else:
                temp = ExpTree(postfix[i])
                temp.rightChild = s.pop()
                temp.leftChild = s.pop()
                s.push(temp)
        return s.peek()

    def preorder(tree):
        s = ''
        if (tree != None):
            s += tree.getRootVal()
            s += ExpTree.preorder(tree.getLeftChild())
            s += ExpTree.preorder(tree.getRightChild())
        return s

    def inorder(tree):
        s = ''
        if (tree != None):
            if (tree.getLeftChild() != None):
                s += '('
            s += ExpTree.inorder(tree.getLeftChild())
            s += tree.getRootVal()
            s += ExpTree.inorder(tree.getRightChild())
            if (tree.getRightChild() != None):
                s += ')'
        return s

    def postorder(tree):
        s = ''
        if (tree != None):
            s += ExpTree.postorder(tree.getLeftChild())
            s += ExpTree.postorder(tree.getRightChild())
            s += tree.getRootVal()
        return s

    def evaluate(tree):
        if (tree.getLeftChild() == None) and (tree.getRightChild() == None):
            return tree.getRootVal()
        left = ExpTree.evaluate(tree.getLeftChild())
        right = ExpTree.evaluate(tree.getRightChild())
        if (str(tree.getRootVal()) in '+-*/'):
            return ExpTree.calculate(left, right, tree.getRootVal())

    def calculate(left, right, operator):
        if (str(operator) == '+'):
            return float(left) + float(right)
        if (str(operator) == '-'):
            return float(left) - float(right)
        if (str(operator) == '*'):
            return float(left) * float(right)
        if (str(operator) == '/'):
            return float(left) / float(right)

    def __str__(self):
        return ExpTree.inorder(self)

# a driver for testing BinaryTree and ExpTree
if __name__ == '__main__':

    # test a BinaryTree

    r = BinaryTree('a')
    assert r.getRootVal() == 'a'
    assert r.getLeftChild()== None
    assert r.getRightChild()== None
    assert str(r) == 'a()()'

    r.insertLeft('b')
    assert r.getLeftChild().getRootVal() == 'b'
    assert str(r) == 'a(b()())()'

    r.insertRight('c')
    assert r.getRightChild().getRootVal() == 'c'
    assert str(r) == 'a(b()())(c()())'

    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    assert str(r) == 'a(b(d()())(e()()))(c(f()())())'

    assert str(r.getRightChild()) == 'c(f()())()'
    assert r.getRightChild().getLeftChild().getRootVal() == 'f'


    # test an ExpTree

    postfix = '5 2 3 * +'
    tree = ExpTree.make_tree(postfix.split())
    assert str(tree) == '(5+(2*3))'
    assert ExpTree.inorder(tree) == '(5+(2*3))'
    assert ExpTree.postorder(tree) == '523*+'
    assert ExpTree.preorder(tree) == '+5*23'
    assert ExpTree.evaluate(tree) == 11.0

    postfix = '5 2 + 3 *'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '((5+2)*3)'
    assert ExpTree.inorder(tree) == '((5+2)*3)'
    assert ExpTree.postorder(tree) == '52+3*'
    assert ExpTree.preorder(tree) == '*+523'
    assert ExpTree.evaluate(tree) == 21.0


