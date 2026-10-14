class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zeros = 1, 0;
        for i in range(len(nums)): 
            if nums[i] != 0: 
                prod *= nums[i]
            else:
                zeros += 1
        
        res = [0] * len(nums)
        if zeros > 1:
            return res

        for i, c in enumerate(nums):
            if zeros:
                if c != 0:
                    res[i] = 0
                else:
                    res[i] = prod
            else: 
                res[i] = prod // c 
        return res


    
            

            