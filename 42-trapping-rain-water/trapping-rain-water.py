class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left = 0
        right = len(height)-1
        
        highest = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] > highest:
                    highest = height[left]
                left+=1
                water += max(0, highest-height[left])
            else:
                if height[right] > highest:
                    highest = height[right]
                right-=1
                water += max(0, highest-height[right])
        return water

        