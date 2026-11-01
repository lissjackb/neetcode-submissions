class TimeMap:

    def __init__(self):
        self.hashTable = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashTable:
            self.hashTable[key] = []
        self.hashTable[key].append((value, timestamp)) 
    
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.hashTable.get(key, [])
        L, R = 0, len(values) - 1
        while L <= R: 
            m = (L+R) // 2 
            if values[m][1] <= timestamp:
                res = values[m][0]
                L = m + 1 
            else:
                R = m - 1
        return res


            
        
