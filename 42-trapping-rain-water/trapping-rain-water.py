class Solution:
    def trap(self, height: List[int]) -> int:
        pre_max = [0] * len(height)
        post_max = [0] * len(height)

        max_height = 0

        # Calculate pre_max
        for i in range(len(height)):
            pre_max[i] = max_height
            max_height = max(max_height, height[i])

        max_height = 0

        # Calculate post_max
        for i in range(len(height) - 1, -1, -1):
            post_max[i] = max_height
            max_height = max(max_height, height[i])

        # print(pre_max)
        # print(post_max)


        ans = []
        for i in range(len(height)):
            ans.append(max(min(pre_max[i],post_max[i])-height[i],0))
            
        # print(ans)
        return sum(ans)
        