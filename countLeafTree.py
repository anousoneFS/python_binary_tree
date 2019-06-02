class Node:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None

    def insert(self, data):
        if data < self.data:   # LEFT
            if self.left:
                self.left = self.left.insert(data)
            else:
                self.left = Node(data)

        else:                   # RIGHT
            if self.right:
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

    def countLeafTree(self):
        if self.left is None and self.right is None:
            return 1

        else:
            if self.left:                  # LEFT
                self.left.countLeafTree()
            else:
                return 0

            if self.right:                 # RIGHT
                self.right.countLeafTree()
            else:
                return 0

        return self.left.countLeafTree() + self.right.countLeafTree()

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is not None:
            self.root.insert(data)
        else:
            self.root = Node(data)

    def preorder(self):
        if self.root:
            self.root.preorder()
        else:
            print("can not preorder (root is empty)")

    def countLeafTree(self):
        if self.root:
            print()
            print(f'count of leaf tree is {self.root.countLeafTree()}')
        else:
            print()
            print("root is empty")

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

    myTree.preorder()

    myTree.countLeafTree()

