class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {}
        L = 0 
        res = 0
        maxfreq = 0

        for R in range(len(s)): 
            chars[s[R]] = 1 + chars.get(s[R],0)
            maxfreq = max(maxfreq, chars[s[R]])
            while (R-L + 1) - maxfreq > k:
                chars[s[L]] -= 1 
                L += 1
            res = max(res, R-L + 1)
        return res 


        