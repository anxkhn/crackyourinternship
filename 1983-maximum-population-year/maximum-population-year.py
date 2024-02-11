class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        birth = []
        death = [] 
        for year in range (101):
            birth.append(0)
            death.append(0)
        for entry in logs:
            birth[entry[0]-1950] += 1
            death[entry[1]-1950] += 1
        births = 0
        deaths = 0
        max = 0
        yr = 0
        for year in range (100):
            births = births + birth[year]
            deaths = deaths + death[year]
            if births-deaths > max:
                max = births-deaths
                yr = year
        return yr+1950