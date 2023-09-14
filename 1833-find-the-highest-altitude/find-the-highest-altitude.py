class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = [0]
        for i in range(len(gain)):
            altitude.append(altitude[i]+gain[i])
        return max(altitude)
        