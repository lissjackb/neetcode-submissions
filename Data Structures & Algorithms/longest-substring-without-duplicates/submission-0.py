class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:  
        L = 0
        length = 0 
        window = set()

        for R in range(len(s)): 
            while s[R] in window: 
                window.remove(s[L])
                L += 1 
            window.add(s[R])
            length = max(R-L + 1, length)
            R += 1
        return length 
        