class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        frequency = [[] for i in range(len(nums)+1)]

        for num in nums: 
            seen[num] = 1 + seen.get(num,0)
        for num, cnt in seen.items(): 
            frequency[cnt].append(num)
        
        output = []
        for i in range(len(frequency) - 1, 0, -1):
            for num in frequency[i]:
                output.append(num)
                if len(output) == k:
                    return output
                 






