class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        cnt = Counter(s)
        maxx = 0
        for i in cnt:
            maxx = max(cnt[i],maxx)
        set_ = set()
        for i in cnt:
            if maxx == cnt[i]:
                set_.add(i)
        print(set_)
        d2= {}
        ss=""
        for char in set_:
            temp = maxx
            for i in range(len(s)):
                if s[i] == char:
                    temp -=1
                if temp == 0:
                    d2[i] = s[i]
                    break
        for i in sorted(d2):
            ss+=d2[i]
        return ss
