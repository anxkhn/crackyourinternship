class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners, first_losers, multiple_losers = set(), set(), set()

        for winner, loser in matches:
            # Add winner.
            if winner not in first_losers and winner not in multiple_losers:
                winners.add(winner)

            # Add or move loser.
            if loser in winners:
                winners.remove(loser)
                first_losers.add(loser)
            elif loser not in first_losers and loser not in multiple_losers:
                first_losers.add(loser)
            elif loser in first_losers:
                first_losers.remove(loser)
                multiple_losers.add(loser)

        return [sorted(list(winners)), sorted(list(first_losers))]
