class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:

        ma = max(nums) 
        mi = min(nums)
        return len(set(nums)) == len(nums) and ma - mi == len(nums) - 1