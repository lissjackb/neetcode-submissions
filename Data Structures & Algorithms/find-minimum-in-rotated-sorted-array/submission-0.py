class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1 
        res = nums[0]

        while L <= R: 
            if nums[L] < nums[R]:
                res = min(res, nums[L])
                break 

            m = (L + R) // 2 
            res = min(res, nums[m])
            if nums[m] >= nums[L]: 
                L = m + 1
            else:
                R = m - 1 
        return res

