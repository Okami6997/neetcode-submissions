class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        s_char = [0] * 26
        for c in s:
            s_char[ord(c) - ord('a')] += 1
        print(s_char)
        w_char = [0] * 26
        for w in wordDict:            
            for c in w:
                w_char[ord(c) - ord('a')] += 1
        print(w_char)
        for i in range(26):
            if w_char == 0 and s_char > 0:
                return False
        return True
