# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        backup = head
        while (head):
            count +=1
            head = head.next
        count = count//2
        ans = []
        head = backup
        while (count != 0):
            head = head.next
            count-=1
        return head
            

        