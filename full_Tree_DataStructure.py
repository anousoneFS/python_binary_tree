i = 0
class Node:
    def __init__(self, data = None):
        self.data = data
        self.right = None
        self.left = None

    def insert(self, data):
        if data == self.data:
            print("can not insert")
        elif data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def preorder(self):
        print(self.data, end=" ")
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data, end=" ")
        if self.right:
            self.right.inorder()
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data, end=" ")

    def find(self, data):
        if data == self.data:
            print(f'yeah tree have {data}')

        elif data < self.data:
            if self.left:
                self.left.find(data)
            else:
                print(f'oh no tree do not have {data}')
        else:
            if self.right:
                self.right.find(data)
            else:
                print(f'oh no tree do not have {data}')

    def delete(self, data):
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
        else:

            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp

            temp = self.right.minValueNode()
            self.data = temp.data
            self.right = self.right.delete(temp.data)

        return self

    def minValueNode(self):

        temp = self
        while temp.left is not None:
            temp = temp.left
        return temp

    def breadthFirstTraversal(self):
        h = self.height()

        for i in range(1, h+1):
            print(f'level {i} :', end=" ")
            self.printBFT(i)
            print()



    def height(self):

        if self.left is None:  # LEFT
            heightLeft = 0
        else:
            heightLeft = self.left.height()


        if self.right is None:  # RIGHT
            heightRight = 0
        else:
            heightRight = self.right.height()


        if heightLeft > heightRight:  # decide
            return heightLeft + 1
        else:
            return heightRight + 1

    def printBFT(self, level):

        if level == 1:
            print(self.data, end=" ")
        else:
            if self.left:
                self.left.printBFT(level - 1)
            if self.right:
                self.right.printBFT(level - 1)

    def countLeafTree(self):
        if self.right is None and self.left is None:
            print(self.data, end=" ")
            global i
            i = i + 1
        else:
            if self.left:
                self.left.countLeafTree()
            if self.right:
                self.right.countLeafTree()


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root.insert(data)

    def preorder(self):
        if self.root:
            print("AFTER PREORDER TRAVERSAL:")
            self.root.preorder()
            print()
        else:
            print("can not preorder")

    def inorder(self):
        if self.root:
            print("AFTER INORDER TRAVERSAL:")
            self.root.inorder()
            print()
        else:
            print("can not inorder")

    def postorder(self):
        if self.root:
            print("AFTER POSTORDER TRAVERSAL:")
            self.root.postorder()
            print()
        else:
            print("can not postorder")

    def find(self, data):
        if self.root:
            self.root.find(data)
        else:
            print("tree is empty")

    def delete(self, data):
        if self.root:
            self.root.delete(data)
        else:
            print("tree is empty")

    def breadthFirstTraversal(self):
        if self.root:
            self.root.breadthFirstTraversal()
            print()

        else:
            print("can not traversal")

    def countLeafTree(self):
        global i
        i = 0
        if self.root:
            print("count of leaf tree is : ")
            self.root.countLeafTree()
            print()
            print(f'numeric is {i}')
        else:
            print("tree is empty")


if __name__ == '__main__':
    t = Tree()
    t.insert(50)
    t.insert(30)
    t.insert(70)
    t.insert(26)
    t.insert(43)
    t.insert(49)
    t.insert(73)
    t.insert(72)
    t.insert(84)
    t.insert(90)

    t.preorder()
    # t.inorder()
    # t.postorder()

    # t.find(34)
    # t.find(30)
    # t.find(99)
    # t.find(26)

    # t.delete(90)
    # t.delete(43)
    # t.delete(73)
    t.preorder()

    t.breadthFirstTraversal()

    t.countLeafTree()