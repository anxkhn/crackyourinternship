class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        key = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_list = []
        for word in words:
            morse = []
            for i in word:
                morse.append(key[ord(i)-97])
            morse_list.append("".join(morse))
        return len(set(morse_list))
