class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nlow = len(nums)//3
        hashh = {}
        final = []
        for i in nums:
            print(hashh)

            if i not in hashh:
                hashh[i] = 1
            else:
                hashh[i] += 1
            if hashh[i] > nlow:
                if i not in final:
                    final.append(i)
        print(hashh)

        return final
            