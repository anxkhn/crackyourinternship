class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def common_factors(num1, num2):
            return sorted(set(i for i in range(1, min(num1, num2) + 1) if num1 % i == num2 % i == 0), reverse=True)
        x = len(str1)
        y = len(str2)
        lst = common_factors(x, y)
        for l in lst:
            first = x//l
            second = y//l
            print(l,first,second)
            if str2[:l]*second == str2:
                if str2[:l]*first == str1:
                    return str2[:l]
        else:
            return ""


        