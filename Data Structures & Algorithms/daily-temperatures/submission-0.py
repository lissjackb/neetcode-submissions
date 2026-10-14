class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        out = [0] * len(temperatures)

        for index, temp in enumerate(temperatures): 
            while stack and temp > stack[-1][1]:
                i, val = stack.pop()
                out[i] = index - i
            stack.append((index, temp))
        return out


                


            