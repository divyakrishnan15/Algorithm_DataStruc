# Node class
class Node:  
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null 

class LinkedList:  # Linked List class contains a Node object
    def __init__(self):# Function to initialize head
        self.head = None 
    def push(self, new_data):  # Function to insert a new node at the beginning
        new_node = Node(new_data)  # 3. Make next of new Node as head
        new_node.next = self.head  # 4. Move the head to point to new Node
        self.head = new_node
    def insertAfter(self, prev_node, new_data):  
        if prev_node is None:# 1. check if the given prev_node exists
            print("The given previous node must inLinkedList.")
            return  
        new_node = Node(new_data)  #  2. create new node & #Put in the data 
        new_node.next = prev_node.next  # 4. Make next of new Node as next of prev_node
        prev_node.next = new_node # 5. make next of prev_node as new_node
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return  
        last = self.head# 5. Else traverse till the last node
        while (last.next):
            last = last.next  
        last.next =  new_node  # 6. Change the next of last node
    def printList(self):# Utility function to print the linked list
        temp = self.head
        while (temp):
            print(temp.data,end=" ")
            temp = temp.next 

if __name__=='__main__':  
    llist = LinkedList()  # Start with the empty list    
    llist.append(6)  # Insert 6.  So linked list becomes 6->None
    llist.push(7)  # Insert 7 at the beginning. So linked list becomes 7->6->None
    llist.push(1) # Insert 1 at the beginning. So linked list becomes 1->7->6->None 
    llist.append(4) # Insert 4 at the end. So linked list becomes 1->7->6->4->None 
    llist.insertAfter(llist.head.next, 8)  # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
    print('Created linked list is: ')
    llist.printList()