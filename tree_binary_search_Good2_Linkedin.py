from dataclasses import dataclass
from turtle import left


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
        
#wrapper class
class Tree:
    def __init__(self,root,name):
        self.root=root
        self.name=name

    def search(self,target):
        return self.root.search(target)

node= Node(10)

node.left = Node(5)
node.right = Node(15)

node.left.left = Node(2)
node.left.right= Node(6)

node.right.left=Node(13)
node.right.right=Node(1000)

print(node.right.data)
print(node.right.right.data)
print("-------------")
mytree=Tree(node,'Div Tree')
print(mytree.name)
print(mytree.root.left.data)
print(mytree.root.right.right.data)
print("-------------")
found = mytree.root.search(2)
print(found.data)