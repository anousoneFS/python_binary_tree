class Node:
    def __init__(self, data=None):
        self.leftChild = None
        self.rightChild = None
        self.data = data

def printPath(node, path = []):
    if node is None:
        return
    path.append(node.data)

    if node.leftChild is None and node.rightChild is None:
        print(" ".join([str(i) for i in path if i != 0]))
    else:
        printPath(node.leftChild, path)
        printPath(node.rightChild, path[0:1])

if __name__ == '__main__':
    root = Node(30)
    root.leftChild = Node(22)
    root.rightChild = Node(45)
    root.leftChild.leftChild = Node(15)
    root.rightChild.rightChild = Node(60)
    root.leftChild.leftChild.leftChild = Node(10)
    root.rightChild.leftChild = Node(40)
    root.rightChild.leftChild.leftChild = Node(35)
    root.rightChild.leftChild.rightChild = Node(42)

    printPath(root)

