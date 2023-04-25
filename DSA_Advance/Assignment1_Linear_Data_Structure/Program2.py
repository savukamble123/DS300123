#2:Reverse a linked list in groups of given size

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data , end = '  ')
            temp = temp.next

    def reverseInGroups(self, head, k):
        current = head
        next = None
        prev = None
        count = 0

        while(current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        if next is not None:
            head.next = self.reverseInGroups(next, k )

        return prev

llist = LinkedList()
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print("Original linked list:")
llist.printList()

head = llist.head
k = 3
llist.head = llist.reverseInGroups(head, k)

print("\nReversed linked list in groups of", k, ":")
llist.printList()
