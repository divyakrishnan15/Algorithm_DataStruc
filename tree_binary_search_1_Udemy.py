from dataclasses import dataclass
from turtle import left

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
node= Node(10)

node.left = Node(5)
node.right = Node(15)

node.left.left = Node(2)
node.left.right= Node(6)

node.right.left=Node(13)
node.right.right=Node(1000)

print(node.right.data)
print(node.right.right.data)

#smaller values to left
#larger values to right

#	         10
#       /  	      \
#     5	            15
#   /   \        /     \
#  2     6      13      1000

#	           5
#       /  	      \
#     3	            7
#   /   \        /     \
#  2     4      6        8