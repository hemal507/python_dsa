class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        n = 0
        c = ''
        for i in s :
            if i.isdigit() :
                n = n*10 + int(i)
            elif i == '[' :
                stk.append((c, n))
                c = ''
                n = 0
            elif i == ']':
                tmp, j = stk.pop()
                c = tmp + c * j
            else: 
                c += i
        return c