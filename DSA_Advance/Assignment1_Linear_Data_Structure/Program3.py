#3:Merge a linked list into another linked list at alternate positions.

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def merge_alternate(head1, head2):
    current1 = head1
    current2 = head2

    while current1 and current2:
        temp = current2.next
        current2.next = current1.next
        current1.next = current2
        current1 = current2.next
        current2 = temp

    return head1

def print_list(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next


list1 = Node(1, Node(3, Node(5)))


list2 = Node(2, Node(4, Node(6, Node(8))))

merged_list = merge_alternate(list1, list2)


print_list(merged_list)
