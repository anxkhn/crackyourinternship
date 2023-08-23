class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ls = []
        for i in range (len(queries)):
            temp = 0
            for j in range (len(points)):
                x = (queries[i][0]-points[j][0])**2 + (queries[i][1]-points[j][1])**2
                if sqrt(x) <= queries[i][2]:
                    temp+=1
                # print(x,queries[i][2],temp)
            ls.append(temp)
        # print(ls)
        return ls

