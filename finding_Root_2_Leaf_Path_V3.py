# version3 was increase index into Node
i = 1
class Node:
    def __init__(self, data=None, index=None):
        self.leftChild = None
        self.rightChild = None
        self.data = data
        self.index = index

    def findIndex(self, data):
        if data < self.data:
            if self.leftChild:
                self.leftChild.findIndex(data)
        elif data > self.data:
            if self.rightChild:
                self.rightChild.findIndex(data)
        else:
            print("index of {} is {}".format(self.data, self.index))
    def insert(self, data):
        global i
        i = 1
        self.insertV2(data)

    def insertV2(self, data):
        global i
        if data == self.data:
            print("can not insert")
        elif data < self.data:
            if self.leftChild:
                i = i + 1
                self.leftChild.insertV2(data)
            else:
                i = i + 1
                self.leftChild = Node(data, i)
        else:
            if self.rightChild:
                i = i + 1
                self.rightChild.insertV2(data)
            else:
                i = i + 1
                self.rightChild = Node(data, i)

def printPath(node, path = []):
    if node is None:
        return
    path.append(node.data)

    if node.leftChild is None and node.rightChild is None:
        print(" ".join([str(j) for j in path if j != 0]))
    else:
        printPath(node.leftChild, path)
        printPath(node.rightChild, path[:node.index])

if __name__ == '__main__':
    root = Node(30, 1)
    # root.leftChild = Node(22, 2)
    # root.rightChild = Node(45, 2)
    # root.leftChild.leftChild = Node(15, 3)
    # root.rightChild.rightChild = Node(60, 3)
    # root.leftChild.leftChild.leftChild = Node(10, 4)
    # root.rightChild.leftChild = Node(40, 3)
    # root.rightChild.leftChild.leftChild = Node(35, 4)
    # root.rightChild.leftChild.rightChild = Node(42, 4)
    root.insert(22)
    root.insert(45)
    root.insert(15)
    root.insert(60)
    root.insert(10)
    root.insert(40)
    root.insert(35)
    root.insert(42)

    printPath(root)
    root.findIndex(30)