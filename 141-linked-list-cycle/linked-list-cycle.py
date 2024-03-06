# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        lst = []
        while head and head.next:
            lst.append(head)
            head = head.next
            if head in lst:
                return True
        return False 
        