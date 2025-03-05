class Solution(object):
    def romanToInt(self,s):
        roman = {"I":1,
                "V":5,
                "X":10,
                "L":50,
                "C":100,
                "D":500,
                "M":1000}
        result = 0
        
        for i in range(len(s)):
            print(i)
            
            if i < len(s)-1 and roman[s[i]]<roman[s[i+1]]:
                result -= roman[s[i]]
            else:
                result += roman[s[i]]  
                
        return result
s = Solution()
print(s.romanToInt("MCMXCIV"))