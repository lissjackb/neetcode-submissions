class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0 
        R = len(nums) - 1 
        
        while L <= R: 
            m = (L + R) // 2 
            if nums[m] == target:
                return m
            
            if nums[L] <= nums[m]:
                if target > nums[m] or target < nums[L]:
                    L = m + 1 
                else: 
                    R = m - 1 
           
            else:
                if target < nums[m] or target > nums[R]:
                    R = m - 1
                else: 
                    L = m + 1

        return -1