class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    def insert(self, data):
        if self.data == data:
            return False   # As BST cannot contain duplicate date
        elif data < self.data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True
    def minValueNode(self, node):
        current = node
        while(current.leftChild is not None):
            current = current.leftChild
        return current

    def delete(self, data):
        if self is None:
            return None
        ''' if current node's data is less than that of root node,
        then only search in left subtree else right subtree'''
        if data < self.data:
            if self.leftChild:
                self.leftChild = self.leftChild.delete(data)
            else:
                print("not found {}".format(data))
        elif data > self.data:
            if self.rightChild:
                self.rightChild = self.rightChild.delete(data)
            else:
                print("not found {}".format(data))
        else:
            # deleting node with one child
            if self.leftChild is None:
                temp = self.rightChild
                self = None
                return temp
            elif self.rightChild is None:
                temp = self.leftChild
                self = None
                return temp
            # deleting node with two children
            # first get the inorder successor
            temp = self.minValueNode(self.rightChild)
            self.data = temp.data
            self.rightChild = self.rightChild.delete(temp.data)
        return self

    def find(self, data):
        if(data == self.data):
            return True
        elif(data < self.data):
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def preorder(self):
        # if self:
            print(str(self.data), end=' ')
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

        # if self:
        #     print(str(self.data), end=' ')
        #     self.leftChild.preorder()
        #     self.rightChild.preorder()


    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.data), end=' ')
            if self.rightChild:
                self.rightChild.inorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.data), end=' ')

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
    def delete(self, data):
        if self.root is not None:
            return self.root.delete(data)
    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False
    def preorder(self):
        if self.root is not None:
            print()
            print('Preorder: ')
            self.root.preorder()
    def inorder(self):
        print()
        if self.root is not None:
            print('Inorder: ')
            self.root.inorder()
    def postorder(self):
        print()
        if self.root is not None:
            print('Postorder: ')
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
    print(tree.find(20))
    print(tree.find(100))

    tree.preorder()
    tree.inorder()
    tree.postorder()
    print('\n\nAfter delete 18')
    # tree.delete(13)
    tree.delete(18)
    tree.preorder()
    tree.inorder()
    tree.postorder()
    # tree.delete(16)
    # print('\n\nAfter delete 16')
    # tree.preorder()
    # tree.inorder()
    # tree.postorder()
