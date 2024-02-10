class Solution:
    def countSubstrings(self, s: str) -> int:
        ## O(n3)
        # count = 0
        # for i in range(len(s)):
        #     for j in range(i + 1, len(s) + 1):
        #         if s[i:j]==s[i:j][::-1]:
        #             count+=1
        # return(count)
        
        ans = 0
        for i in range(len(s)):
            l = r = i
            # odd pali
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
            # even pali
            l = i
            r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
        return ans