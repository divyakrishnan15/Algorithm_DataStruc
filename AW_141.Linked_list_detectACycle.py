class Node:
	# Constructor to initialize
	# the node object
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	# Function to initialize head
	def __init__(self):
		self.head = None

	# Function to insert a new
	# node at the beginning
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# Utility function to print it
	# the linked LinkedList
	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data, end=" ")
			temp = temp.next

	def detectLoop(self):
		s = set()
		temp = self.head
		while (temp):

			# If we have already has
			# this node in hashmap it
			# means their is a cycle
			# (Because you we encountering
			# the node second time).
			if (temp in s):
				return True

			# If we are seeing the node for
			# the first time, insert it in hash
			s.add(temp)

			temp = temp.next

		return False


# Driver program for testing
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)

# Create a loop for testing
llist.head.next.next.next = llist.head

if(llist.detectLoop()):
	print("Loop found")
else:
	print("No Loop ")

# This code is contributed by Gitanjali.

# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
