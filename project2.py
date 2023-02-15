
# Name: Aiden Nelson, eid: 800742353
# Date of Start: 2/15/2023
# Date of Last Edit: 2/15/2023

from os import listdir
from os.path import isfile, join

loop = True

class TreeNode:
    def __init__(self, parent, value, color):
        self.parent = parent
        self.value = value
        self.left, self.right = None, None
        self.color = color
    
    
def buildRBT(filePath):
    print("buildRBT")


def buildBST(filePath) -> TreeNode:
    f = open(filePath, 'r')
    first = True
    root = None
    for num in f:
        if(first):
            root = TreeNode(None, int(num), None)
            first = False
        else:
            node = TreeNode(None, int(num), None)
            Insert(root, node)
    
    InOrderTreeTraversal(root)
    
    print("Parent of key  7 is: ")
    PrintParentKey(root, 7)
    return

def InOrderTreeTraversal(node:TreeNode):
    if(node):
        InOrderTreeTraversal(node.left)
        print(node.value, node.left.value if node.left else "None", node.right.value if node.right else "None")
        InOrderTreeTraversal(node.right)
    return

def Search(node:TreeNode, target:int):
    if not node:
        return False

    if node.value == target:
        return True
    
    return Search(node.left, target) if node.value > target else Search(node.right, target)

def Insert(root:TreeNode, node:TreeNode):
    y = None
    x = root
    while x:
        y = x
        if(node.value < x.value):
            x = x.left
        else:
            x = x.right
    
    node.parent = y

    if node.value < y.value:
        y.left = node
    else:
        y.right = node

def PrintParentKey(node:TreeNode, value:int):
    if not node:
        print("NIL")
        return

    if node.value == value:
        print(node.parent.value if node.parent else "NIL")
        return
    return PrintParentKey(node.left, value) if node.value > value else PrintParentKey(node.right, value)

def PrintLeftChild(root:TreeNode, value:int):
    #Maybe make function to return node, would make code easier for sure.
    return

while(loop):

    files = [f for f in listdir() if isfile(f)]

    fileName = input("What file would you like to build from? \n")

    if fileName in files:
        print("\nAnalyzing ", fileName, "\n")
        treeType = input("BST (B) or RB-Tree (R)? \n")
        if treeType in ['B', 'R']:
            print("\nBuilding a ", ("BST" if treeType == 'B' else "RB-Tree"), " from fileName. \n")
            if treeType == 'B':
                buildBST(fileName)
            else:
                buildRBT(fileName)
        else:
            print("Bad tree type. Try again.\n\n")
    else:
        print("Bad file. Try again.")

