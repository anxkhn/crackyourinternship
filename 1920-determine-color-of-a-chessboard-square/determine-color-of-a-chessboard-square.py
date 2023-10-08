class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if (ord(coordinates[0])-96) % 2 != 0:
            return (int(coordinates[1])+1) % 2
        else:
            return int(coordinates[1]) % 2
        