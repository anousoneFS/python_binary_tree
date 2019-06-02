import copy
t = 0
class Node:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None
    def insert(self, data):
        if data == self.data:
            print("can not insert")
        # LEFT
        elif data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        # RIGHT
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)
        return self
    def preorder(self):
        print(self.data, end=' ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    def minValueNode(self, node):
        current = node
        while(current.left is not None):
            current = self.left
        return current

    def delete(self, data):
        # find at LEFT
        if data < self.data:
            self.left = self.left.delete(data)
        # find at RIGHT
        elif data > self.data:
            self.right = self.right.delete(data)
        # found
        else:
            # deleting node
            # if node have one node or nothing
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp

            # if node have two nodes
            temp = self.minValueNode(self.right)
            self.data = temp.data
            self.right = self.right.delete(temp.data)

        return self

    def root2Leaf(self):
        print(self.data, end=' ')
        if self.right or self.left:
            if self.left:
                self.left = self.left.root2Leaf()
            else:
                self.right = self.right.root2Leaf()
            if self.left is None and self.right is None:
                self = None
        # delete leaf node
        else:
            self = None
            print()
        return self

    def countLeafTree(self):
        global t
        if self.left is None and self.right is None:
            t = t + 1
            return t
        else:
            if self.left:                  # LEFT
                self.left.countLeafTree()
            if self.right:                 # RIGHT
                self.right.countLeafTree()

        return t

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
            print("")
            print("AFTER PREORDER TRAVERSAL: ")
            self.root.preorder()
        else:
            print("root is empty")

    def delete(self, data):
        if self.root:
            self.root.delete(data)
        else:
            print("can not delete because tree is empty")

    def root2Leaf(self):
        if self.root:
            t = self.root.countLeafTree()
            print(f'count of leaf Node is {t}')
            cpt = copy.deepcopy(self.root)
            for i in range(t):
                cpt.root2Leaf()
        else:
            print("root is empty")

if __name__ == '__main__':
    tree = Tree()
    tree.insert(30)
    tree.insert(22)
    tree.insert(45)
    tree.insert(15)
    tree.insert(28)
    tree.insert(60)
    tree.insert(50)
    tree.insert(10)
    tree.insert(16)
    tree.insert(55)
    tree.insert(70)
    tree.preorder()

    # tree.delete(50)
    # tree.delete(22)
    tree.preorder()
    print()
    tree.root2Leaf()
    tree.preorder()
