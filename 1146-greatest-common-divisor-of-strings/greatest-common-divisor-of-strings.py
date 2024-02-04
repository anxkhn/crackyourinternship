class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def common_factors(num1, num2):
            common_factors_set = set()
            min_num = min(num1, num2)
            for i in range(1, min_num + 1):
                if num1 % i == num2 % i == 0:
                    common_factors_set.add(i)
            return sorted(list(common_factors_set), reverse=True)
        x = len(str1)
        y = len(str2)
        lst = common_factors(x, y)
        for l in lst:
            first = x//l
            second = y//l
            if str2[:l]*second == str2 and str2[:l]*first == str1:
                return str2[:l]
        else:
            return ""


        