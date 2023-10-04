class Solution:
    def minimumSum(self, num: int) -> int:
        lst = []
        x = str(num)
        for i in x:
            lst.append(int(i))
        lst.sort()
        a = lst[0]*10+lst[-1]
        b = lst[1]*10+lst[-2]

        return a+b