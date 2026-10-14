class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = []
        for string in strs:
            i = len(string)
            encode.append(str(i))
            encode.append("#")
            encode.append(string)
        return "".join(encode)

    def decode(self, s: str) -> List[str]:
        decode = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j]) 
            i = j + 1
            j = i + length
            decode.append(s[i:j])
            i = j 

        return decode

        
