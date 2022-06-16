from logging.config import valid_ident


class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

def make_list(elements):
    head = ListNode(elements[0])
    for element in elements[1:]:
        ptr = head
        while ptr.next:
            ptr = ptr.next
        ptr.next = ListNode(element)
    return head

def print_list(head):
    ptr = head
    print('[', end = "")
    while ptr:
        print(ptr.val, end = ", ")
        ptr = ptr.next
    print(']')

def merge2lists(L1,L2):
    dummy = ListNode()
    tail  = dummy

    while L1 and L2:
        if L1.val <L2.val:
            tail.next = L1
            L1        = L1.next
        else:
            tail.next = L2
            L2        = L2.next
        tail = tail.next

        if L1:
            tail.next = L1
        elif L2:
            tail.next = L2

        return dummy.next


L1=[1,2,4]
L2=[1,3,4]
    
    
print_list(merge2lists(make_list(L1)),(make_list(L2)))