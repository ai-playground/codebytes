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

    def reverse(self,start,stop):
        """
        this function performs in place inversion from start_node to stop_node

        Args:
        start(int) = node where invertion should start
        stop(int) = node where invertion should stop
        head_node is considered 0th node, if there are 4 nodes in the linkedlist
        along with head node, start_node = 1, stop_node = 3

        Return:
        head_node as before after reverse
        """
        start_node = self.head
        #lp, mp, rp = None
        count = 0

        while start_node and count < start-1:
            start_node = start_node.next
            count += 1

        buffer_node = start_node.next

        lp = start_node.next
        mp = lp.next
        rp = mp.next

        while rp and count < stop-1:
            count += 1
            mp.next = lp

            lp = mp
            mp = rp
            rp = rp.next

        start_node.next = lp
        buffer_node.next = mp
