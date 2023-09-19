class Node:
    def __init__(self, val = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, index: int) -> int:
        if index >= self.size: # invalid index
            return -1
            
        cur = self.head
        for _ in range(index+1):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:  # invalid index
            return

        prev = self.head
        for _ in range(index):
            prev = prev.next

        # insert `newNode` between `prev` and `prev.next`
        newNode = Node(val, prev.next, prev)
        prev.next.prev = newNode
        prev.next = newNode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:  # invalid index
            return

        prev = self.head
        for _ in range(index):
            prev = prev.next

        nxt = prev.next.next
        prev.next = nxt
        nxt.prev = prev
        self.size -= 1