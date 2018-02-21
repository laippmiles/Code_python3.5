class Solution(object):
    def reverseVowels(self, s):
        str = ['a','e','i','o','u','A','E','I','O','U']
        VowelsInStr = []
        Ans = []
        for w in s[::-1]:
            if w in str:
                VowelsInStr.append(w)
        count = 0
        for n in s:
            if n in str:
                Ans.append(VowelsInStr[count])
                count += 1
            else:
                Ans.append(n)
        return ''.join(Ans)
