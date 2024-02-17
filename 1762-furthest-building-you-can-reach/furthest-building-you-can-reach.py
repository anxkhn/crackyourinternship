class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # diffs = []
        # for i in range(len(heights)-1):
        #     diffs.append(max(0, heights[i+1] - heights[i]))
        # for i in range(len(heights)-1):
        #     if sum(diffs[:i+1]) - sum(sorted(diffs[:i+1], reverse=True)[:ladders]) > bricks:
        #         return i
        # return i + 1
        n = len(heights)
        heap = []
        bricks_used = 0
        
        for i in range(n - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heapq.heappush(heap, diff)
                if len(heap) > ladders:
                    bricks_used += heapq.heappop(heap)
                if bricks_used > bricks:
                    return i
        
        return n - 1

