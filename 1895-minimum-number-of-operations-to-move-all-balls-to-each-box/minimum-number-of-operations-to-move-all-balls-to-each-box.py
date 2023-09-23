class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        ans2 = []

        for i in range(len(boxes)):
            count = 0
            for j in range(i,len(boxes)):
                if int(boxes[j]) == 1:
                    count += j-i
            ans.append(count)

        for i in range(len(boxes)-1,-1,-1):
            count = 0
            for j in range(i-1,-1,-1):
                # print(i,j)
                if int(boxes[j]) == 1:
                    count += i-j
            ans2.append(count)
        # print(ans,ans2)
        for i in range(len(boxes)):
            ans[i] += ans2[::-1][i]
        return ans