class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value
def inorder(node):
    if(node is not None):
        inorder(node.left)
        print(node.data)
        inorder(node.right)
root = Node(4)

root.left = Node(5)
root.right = Node(6)

root.left.left = Node(7)

inorder(root) 
#'Ans = 7 5 4 6'
'''
7 becomes left child of 5
		           4 ~
		       /       \ 
		      5	        6 
	      /  \      /   \ 
       7   None  None  None
      / \
  None   None
'''


''' following is the tree after above statement 
	    4 
	  /   \ 
	None  None
'''

''' 5 and 6 become left and right children of 1 
		           4 
		       /       \ 
		      5	        6 
	      /  \      /   \ 
      None None  None  None
'''

