class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data == self.data:
            return
        elif data < self.data:  # LEFT
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
        else:                    # RIGHT
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
        return

    def find(self, data):
        if data == self.data:
            return True
        elif data < self.data:   # find at left
            if self.left:         # found node
                return self.left.find(data)
            else:                 # not found
                return False
    # -------------------------------------------------
        else:                   # find at right
            if self.right:      # found node
                return self.right.find(data)
            else:                # not found
                return False

    def preorder(self):
        print(str(self.data), end=' ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(str(self.data), end=' ')
        if self.right:
            self.right.inorder()
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(str(self.data), end=' ')

    def minValueNode(self):
        while(self != None):
            temp = self
            self = self.left
        return temp

    def delete(self, data):
       if data < self.data:      # LEFT
           self.left = self.left.delete(data)

       elif data > self.data:     # RIGHT
           self.right = self.right.delete(data)

       else:  # deleting with one child

           if self.left is None:    # if don't have left node
                temp = self.right
                self = None
                return temp
           elif self.right is None:   # if don't have right node
                temp = self.left
                self = None
                return temp

           # deleting with two child

           temp = self.right.minValueNode()
           self.data = temp.data
           self.right.delete(temp.data)

       return self


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            print(self.root.find(data))
        else:
            print("empty tree")
    def preorder(self):
        if self.root:
            print()
            print("preorder Traversal: ")
            self.root.preorder()
        else:
            print("can not preorder Traversal")
    def inorder(self):
        if self.root:
            print()
            print("inorder Traversal: ")
            self.root.inorder()
        else:
            print("can not inorder Traversal")
    def postorder(self):
        if self.root:
            print()
            print("postorder Traversal: ")
            self.root.postorder()
        else:
            print("can not postorder Traversal")

    def delete(self, data):
        if self.root:
            return self.root.delete(data)
        else:
            print("empty tree")

if __name__ == '__main__':
    myTree = Tree()
    myTree.insert(16)
    myTree.insert(11)
    myTree.insert(18)
    myTree.insert(10)
    myTree.insert(26)
    myTree.insert(14)
    myTree.insert(13)
    myTree.insert(26)
    myTree.insert(21)
    myTree.insert(20)
    myTree.insert(20)
    # myTree.find(20)
    # myTree.find(30)
    # myTree.find(100)
    # myTree.find(14)

    myTree.preorder()
    myTree.inorder()
    myTree.postorder()

    myTree.delete(21)
    myTree.preorder()