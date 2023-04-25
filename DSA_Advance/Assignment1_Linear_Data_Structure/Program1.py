#1:Delete the elements in an linked list whose sum is equal to zero
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data, end=' ')
            curr_node = curr_node.next
        print()

    def delete_zero_sum(self):
        curr_node = self.head
        sums = [0]
        while curr_node is not None:
            sums.append(sums[-1] + curr_node.data)
            curr_node = curr_node.next
        prefix_sum = {}
        curr_node = self.head
        i = 0
        while curr_node is not None:
            if sums[i] in prefix_sum:
                prefix_node = prefix_sum[sums[i]]
                prefix_node.next = curr_node.next
                if prefix_node.next is not None:
                    i -= 1
                    curr_node = prefix_node.next
                else:
                    curr_node = None
                    self.head = None
            else:
                prefix_sum[sums[i]] = curr_node
                curr_node = curr_node.next
                i += 1


llist = LinkedList()
llist.insert(6)
llist.insert(3)
llist.insert(-9)
llist.insert(2)
llist.insert(-3)
llist.insert(1)
print("Original List:")
llist.display()
llist.delete_zero_sum()
print("List after deleting zero sum elements:")
llist.display()
