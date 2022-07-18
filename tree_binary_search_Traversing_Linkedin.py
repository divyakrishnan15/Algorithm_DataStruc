from dataclasses import dataclass
from turtle import left
from xml.dom.minicompat import NodeList


class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    def search(self,target):
        if self.data==target:
            print("Foundit !")
            return self
        if self.left and self.data > target:
            return self.left.search(target)

        if self.right and self.data < target:
            return self.right.search(target)

        print("Value is not in tree")

    def height(self,h=0):
        left_height=self.left.height(h+1) if self.left else h
        right_height=self.right.height(h+1) if self.right else h
        return max(left_height,right_height)


    def preOrder(self):
        print(self.data)
        if self.left:
            self.left.preOrder()

        if self.right:
            self.right.preOrder()
    
    def inOrder(self):        
        if self.left:
            self.left.inOrder()
        print(self.data)
        if self.right:
            self.right.inOrder()

    def postOrder(self):        
        if self.left:
            self.left.postOrder()

        if self.right:
            self.right.postOrder()
        print(self.data)

    def getNodesAtDepth(self,depth,node=[]):
        if depth == 0:
            nodes.append(self.data)
            return node
        
        if self.left:
            self.left.getNodesAtDepth(depth-1,node)
        else:
            node.extend([None]*2**(depth-1))
        if self.right:
            self.right.getNodesAtDepth(depth-1,node)
        else:
            node.extend([None]*2**(depth-1))
#wrapper class
class Tree:
    def __init__(self,root,name):
        self.root=root
        self.name=name

    def search(self,target):
        return self.root.search(target)

    def preOrder(self):
        self.root.preOrder()
    def inOrder(self):
        self.root.inOrder()
    def postOrder(self):
        self.root.postOrder()
    def height(self):
        return self.root.height()
    def getNodesAtDepth(self,depth):
        return self.root.getNodesAtDepth(depth)

node= Node(10)

node.left = Node(5)
node.right = Node(15)

node.left.left = Node(2)
node.left.right= Node(6)

node.right.left=Node(13)
node.right.right=Node(1000)

print("-------------")
print("node data")
print("-------------")
print(node.right.data)
print(node.right.right.data)
print("-------------")
print("obj of class Node data")
print("-------------")
mytree=Tree(node,'Div Tree')
print(mytree.name)
print(mytree.root.left.data)
print(mytree.root.right.right.data)
print("-------------")
print("If node is there in tree")
print("-------------")
found = mytree.root.search(2)
print(found.data)
print("-------------")
print("PRE ORDER")
mytree.preOrder()
print("IN ORDER")
mytree.inOrder()
print("POST ORDER")
mytree.postOrder()
print("-------------")
print("Node's height")
print("-------------")
print(mytree.root.height())
mytree=Tree(Node(5),'Tree height')
print(mytree.root.height())
print("-------------")
print("Node's at DEPTH")
print("-------------")
print(mytree.getNodesAtDepth(2))
