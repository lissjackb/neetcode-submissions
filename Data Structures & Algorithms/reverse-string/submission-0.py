class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        L = 0
        R = len(s) - 1 

        while L < R:
            sl = s[L] 
            rl = s[R]
            s[L] = rl
            s[R] = sl
            L += 1 
            R -= 1

        