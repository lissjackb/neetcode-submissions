class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        q = deque(students)
        size = len(students)

        res = size
        for sandwich in sandwiches:
            cnt = 0 
            while cnt < size and q[0] != sandwich:
                cur = q.popleft()
                q.append(cur)
                cnt += 1
            
            if q[0] == sandwich:
                q.popleft()
                res -= 1 
            else: 
                break 
        return res
