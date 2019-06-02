class Node:
    def __init__(self, data=None):
        self.right = None
        self.left = None
        self.data = data

    def insert(self, data):
        if data == self.data:
            print("can not insert")
        elif data < self.data:   # LEFT
            if self.left is not None:
                self.left = self.left.insert(data)
            else:
                self.left = Node(data)

        else:                   # RIGHT
            if self.right is not None:
                self.right = self.right.insert(data)
            else:
                self.right = Node(data)

        return self
    def preorder(self):
        print(self.data, end=' ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def height(self):
        if self.left is None:     # LEFT
            heightLeft = 0
        else:
            heightLeft = self.left.height()
    # -------------------------------------
        if self.right is None:     # RIGHT
            heightRight = 0
        else:
            heightRight = self.right.height()
    # ----------------------------------------
        if heightLeft > heightRight:   # decide
            return heightLeft + 1
        else:
            return heightRight + 1

    def breadthFirstTraversal(self):
        h = self.height()
        for i in range(1, h+1):
            self.printBFT(i)

    def printBFT(self, level):
        if level is 1:
            print(self.data, end=' ')

        else:
            if self.left is not None:
                self.left.printBFT(level - 1)

            if self.right is not None:
                self.right.printBFT(level - 1)


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root.insert(data)
    def preorder(self):
        if self.root is not None:
            print()
            print("PREORDER TRAVERSAL: ")
            self.root.preorder()
    def breadthFirstTraversal(self):
        if self.root is not None:
            print()
            self.root.breadthFirstTraversal()
        else:
            print("can not print")
    def h(self):
        a = self.root.height()
        print()
        print(a)
if __name__ == '__main__':
    myTree = Tree()
    myTree.insert(35)
    myTree.insert(13)
    myTree.insert(72)
    myTree.insert(9)
    myTree.insert(16)
    myTree.insert(54)
    myTree.insert(83)
    myTree.insert(7)
    myTree.insert(24)
    myTree.insert(55)
    myTree.insert(17)
    myTree.insert(60)
    myTree.insert(57)
    myTree.insert(19)
    myTree.insert(20)
    myTree.preorder()

    myTree.breadthFirstTraversal()
    myTree.h()