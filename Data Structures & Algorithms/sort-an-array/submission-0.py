class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
       
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left_half = merge_sort(arr[:mid])
            right_half = merge_sort(arr[mid:])

            sorted_arr = []
            i = j = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    sorted_arr.append(left_half[i])
                    i += 1
                else:
                    sorted_arr.append(right_half[j])
                    j += 1

            while i < len(left_half):
                sorted_arr.append(left_half[i])
                i += 1

            while j < len(right_half):
                sorted_arr.append(right_half[j])
                j += 1

            return sorted_arr

        return merge_sort(nums)