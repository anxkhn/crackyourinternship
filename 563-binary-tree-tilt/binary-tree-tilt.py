# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def helper(root):
            if not root: 
                return 0
            lv = helper(root.left)
            rv =  helper(root.right)
            self.ans += abs(lv - rv)
            return root.val + lv + rv
        helper(root)
        return self.ans

        