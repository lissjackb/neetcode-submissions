class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
       
        for s in strs:
            count = [0] * 26 
            for c in s: 
                count[ord(c) - ord('a')] += 1
            if tuple(count) not in anagrams:
                anagrams[tuple(count)] = []
            anagrams[tuple(count)].append(s)
        return list(anagrams.values())
                 
            
            
            


    
        