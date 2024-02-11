# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        backup = head
        while (head):
            count +=1
            head = head.next
        if count < 2:
            return head
        count = count//2
        head = backup
        while (count != 1):
            head = head.next
            count-=1
        head.next = head.next.next
        return backup

        