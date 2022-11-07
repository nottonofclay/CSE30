class BinaryTree:

    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        if self.rightChild == None:
            return ''
        else:
            return self.rightChild

    def getLeftChild(self):
        if self.leftChild == None:
            return ''
        return self.leftChild

    def getRootVal(self):
        return self.key

    def setRootVal(self, obj):
        self.key = obj

    def __str__(self):
        return (f'{self.key}[{self.getLeftChild()}][{self.getRightChild()}]')


if __name__ == '__main__':
    r = BinaryTree('a')
    print(r) # a
    r.insertLeft('b')
    r.insertRight('c')
    print(r) # a[b[][]][c[][]]
    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    print(r) # a[b[d[][]][e[][]]][c[f[][]][]]
    print(r.getRootVal()) # a
    print(r.getLeftChild()) # b[d[][]][e[][]]
    print(r.getRightChild()) # c[f[][]][]