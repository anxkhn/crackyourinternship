class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        winners, losers = {}, {}

        for match in matches:
            if match[0] not in winners:
                winners[match[0]] = 1
            else:
                winners[match[0]] += 1
            if match[1] not in losers:
                losers[match[1]] = 1
            else:
                losers[match[1]] += 1

        res_1, res_2 = [], []

        for k, v in winners.items():
            if k not in losers:
                res_1.append(k)
        
        for k, v in losers.items():
            if v == 1:
                res_2.append(k)

        res_1.sort()
        res_2.sort()
        
        return [ res_1, res_2 ]