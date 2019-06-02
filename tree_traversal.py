class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data
    def setLeft(self, node):
        self.left = node
    def setRight(self, node):
        self.right = node
    def setData(self, data):
        self.data = data
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right
    def getData(self):
        return self.data

def preorder(Tree):
    if Tree:
        print(Tree.getData(), end=" ")
        preorder(Tree.getLeft())
        preorder(Tree.getRight())
    return

def inorder(Tree):
    if Tree:
        inorder(Tree.getLeft())
        print(Tree.getData(), end=" ")
        inorder(Tree.getRight())
    return

def postorder(Tree):
    if Tree:
        postorder(Tree.getLeft())
        postorder(Tree.getRight())
        print(Tree.getData(), end=" ")
    return

if __name__ == '__main__':
    root = Node('R')
    root.setLeft(Node('A'))
    root.setRight(Node('B'))
    root.left.setLeft(Node('C'))
    root.left.setRight(Node('D'))
    root.left.left.setLeft(Node('F'))
    root.right.setLeft(Node('E'))
    root.right.left.setLeft(Node('G'))
    root.right.left.setRight(Node('H'))

    print("Preorder Traversal:")
    preorder(root)
    print("\n inorder Traversal:")
    inorder(root)
    print("\n Postorder Traversal:")
    postorder(root)
    print("")
    print(root.getData())
    print(root.left.getData())
    print(root.left.right.getData())