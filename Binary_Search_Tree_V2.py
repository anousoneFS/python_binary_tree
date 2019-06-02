class Node:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None

    def insert(self, data):
        if data == self.data:
            return False
        # left Node
        elif data < self.data:
            if self.left:      # there is left Node
                return self.left.insert(data)     # find again
            else:            # do not left Node
                self.left = Node(data)       # build left Node
                # return True

        # right Node
        else:
            if self.right:    # there is right Node
                return self.right.insert(data)  # find again
            else:            # do not right Node
                self.right = Node(data)       # build right Node
                # return True
    def preorder(self):
        print(str(self.data), end=" ")
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
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

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is not None:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
    def preorder(self):
        if self.root is not None:
            print()
            print("preorder Traversal: ")
            self.root.preorder()
    def inorder(self):
        if self.root:
            print()
            print("inorder Traversal: ")
            self.root.inorder()
    def postorder(self):
        if self.root:
            print()
            print("postorder Traversal: ")
            self.root.postorder()

if __name__ == '__main__':
    tree = Tree()
    tree.insert(16)
    tree.insert(18)
    tree.insert(11)
    tree.insert(10)
    tree.insert(26)
    tree.insert(14)
    tree.insert(13)
    tree.insert(21)
    tree.insert(20)

    tree.preorder()
    tree.inorder()
    tree.postorder()