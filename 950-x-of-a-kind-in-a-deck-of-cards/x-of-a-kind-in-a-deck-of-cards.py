class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) < 2:
            return False
        
        frequency = collections.Counter(deck)
        gcd = frequency[deck[0]]
        
        for count in frequency.values():
            gcd = math.gcd(gcd, count)
        
        return gcd >= 2
