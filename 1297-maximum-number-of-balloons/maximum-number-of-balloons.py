class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # hash_map = {}
        # hash_map["b"] = 0
        # hash_map["a"] = 0
        # hash_map["l"] = 0
        # hash_map["o"] = 0
        # hash_map["n"] = 0
        hash_map = {char: 0 for char in "balloon"}
        for i in text:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1
        return min(hash_map["b"],hash_map["a"],hash_map["l"]//2,hash_map["o"]//2,hash_map["n"])
