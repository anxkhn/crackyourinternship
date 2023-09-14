class Solution:
    def candy(self, ratings: List[int]) -> int:
        lenght = len(ratings)
        candies = [1] * lenght
        for i in range(1,lenght):
            if ratings[i] > ratings[i-1]:
                candies[i]=candies[i-1]+1
        # print(candies)
        
        for i in range(lenght-1,0,-1):
            if ratings[i] < ratings[i-1]:
                if candies[i-1] <= candies[i]:
                    candies[i-1]=candies[i]+1
        # print(candies)
        return sum(candies)