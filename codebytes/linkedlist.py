class ListNode:
    def __init__(self,data=0,next=None):
        self.data = data
        self.next = next
    def get_data(self):
        return self.data
    def set_data(self,data=0):
        self.data = data
    def get_next(self):
        return self.next
    def set_next(self,next=None):
        self.next = next

class List:
    def __init__(self):
        self.head = ListNode()

    def insert(self,data=0):
        node = ListNode(data)
        node.set_next(self.head.next)
        self.head.set_next(node)

    def delete(self,data):
        node = self.head
        while node.next and node.next.data != data:
            node = node.next
        node = node.next.next

    def print(self):
        node = self.head
        while node:
            print(node.data,end="->")
            node = node.next
        print("\n")
