class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        res = set()
        for s in words:
            sort_odd_even = ''.join(sorted(s[1::2]) + sorted(s[::2]))
            res.add(sort_odd_even)
        print(res)
        return len(res)

        