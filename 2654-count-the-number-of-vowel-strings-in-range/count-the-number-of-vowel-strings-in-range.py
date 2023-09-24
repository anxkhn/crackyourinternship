class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0

        vowels=['a','e','i','o','u']

        for i in range(left,right+1):

            if words[i][-1] in vowels and words[i][0] in vowels:

                count += 1

        return count
