class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        s_char = [0] * 26
        for c in s:
            s_char[ord(c) - ord('a')] += 1
        for w in wordDict:
            w_char = [0] * 26
            ch = s_char
            for c in w:
                ch[ord(c) - ord('a')] -= 1
                if ch[ord(c) - ord('a')] == -1:
                    return False
        return True
