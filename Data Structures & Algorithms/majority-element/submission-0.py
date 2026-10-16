class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}
        for val in nums:
            seen[val] = seen.get(val, 0) + 1

        max_count = 0
        max_val = None
        for val, count in seen.items():
            if count > max_count:
                max_count = count
                max_val = val
        return max_val
