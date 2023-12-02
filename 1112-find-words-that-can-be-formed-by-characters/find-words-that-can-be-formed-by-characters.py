class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)
        total = 0
        for word in words:
            word_count = Counter(word)
            x = len(word)
            y = 0
            for char in word_count:
                if word_count[char] > char_count[char]:
                    break
                y+=word_count[char]
            if x == y:
                total+=x
        return total

            