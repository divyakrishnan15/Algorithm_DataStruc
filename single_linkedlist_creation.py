class Node:
    def __init__(self,data):
        #value of the nodes are in data
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        #' create an empty list'
        self.head=None 
    
    def printLinkedList(self):
        #tmp is at the head of the list
        tmp=self.head
        #link_list variable ..this is the list to print
        link_list_var =""

#until tmp is valid
        while tmp:
            link_list_var +=(str(tmp.data) + " ")
            tmp=tmp.next
        print(link_list_var)
#5=> 1=>3 => 7

link_list_var=Linkedlist()
link_list_var.head=Node(5)

sec_node =Node(1)
third_node=Node(3)
fourth_node=Node(7)

link_list_var.head.next=sec_node
sec_node.next=third_node
third_node.next=fourth_node

link_list_var.printLinkedList()