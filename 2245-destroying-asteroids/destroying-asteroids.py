class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # brute OG
        # asteroids.sort()
        # if mass < asteroids[0]:
        #     return False
        # order = []
        # for i in range(len(asteroids)-1):
        #     if i == 0:
        #         order.append(mass+asteroids[i])
        #     else:
        #         order.append(order[-1]+asteroids[i])
        #         if order[-1] < asteroids[i+1]:
        #             return False
        # print(asteroids,order)
        # return True 

        # Time: O(n * log(n)), space: O(n) - including sorting space.
        
        for a in sorted(asteroids):
            if mass < a:
                return False
            mass += a
        return True

