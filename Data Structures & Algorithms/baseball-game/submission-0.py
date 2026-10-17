class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()

        for val in operations:
            if val == "+":
                val1 = stack[-1]
                val2 = stack[-2]
                stack.append(val1 + val2)
            elif val == "D":
                val1 = stack[-1]
                stack.append(val1 * 2)
            elif val == "C":
                stack.pop()
            else:
                stack.append(int(val))
        
        total = 0
        for val in stack: 
            total += val
        
        return total 



            
        