class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = Counter(s1)
        window = Counter(s2[:len(s1)])
        
        if window == s1_count:
            return True
            
        for R in range(len(s1), len(s2)):
            window[s2[R]] += 1
            window[s2[R - len(s1)]] -= 1
            if window == s1_count:
                return True
                
        return False