class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = 0
        curr = 0
        R = len(nums) - 1

        while curr <= R:
            if nums[curr] == 0:
                nums[L], nums[curr] = nums[curr], nums[L]
                L += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[R] = nums[R], nums[curr]
                R -= 1
            else:
                curr += 1