class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        temp = set(nums1)
        set2 = set(nums2)
        for i in nums2:
            set1.discard(i)
        for i in temp:
            set2.discard(i)
        return [list(set1),list(set2)]
        