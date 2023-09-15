class ListNode:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value) -> None:
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def append_values(self, values) -> None:
        tail_node = self.head
        while tail_node.next:
            tail_node = tail_node.next

        for value in values:
            if not tail_node:
                tail_node = ListNode(value)
            else:
                tail_node.next = ListNode(value)
                tail_node = tail_node.next

    def print_list(self) -> None:
        node = self.head
        while node:
            print("%s" % node.data, end = " -> ")
            node = node.next
        print()

