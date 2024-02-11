# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        val = ""
        while (head.next):
            val += str(head.val)
            head = head.next
        val += str(head.val)
        return int(val, 2) 
        