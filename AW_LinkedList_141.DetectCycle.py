class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    # Function to reverse the linked list
    def Cycle(self,head):
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

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
 
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
 
 
# Driver code
llist = LinkedList()
llist.push(3)
llist.push(2)
llist.push(0)
llist.push(-4)

# Create a loop for testing
llist.head.next.next.next.next = llist.head

pos=-1
 
print("Given Linked List")
llist.printList()
llist.Cycle()
print("\nReversed Linked List")
llist.printList()