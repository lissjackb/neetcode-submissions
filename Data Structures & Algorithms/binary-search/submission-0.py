class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while L <= R: 
            midd = (L + R) // 2

            if nums[midd] < target: 
                L = midd + 1
            elif nums[midd] > target:
                R = midd - 1 
            else:
                return midd
        return -1