#百度C++改过来的
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        c = [
            ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
            ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
            ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
            ["", "M", "MM", "MMM"]
        ]
        roman = []
        roman.append(c[3][num / 1000 % 10])
        roman.append(c[2][num / 100 % 10])
        roman.append(c[1][num / 10 % 10])
        roman.append(c[0][num % 10])
        return ''.join(roman)

# 88ms的版本
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        M = ["", "M", "MM", "MMM"];
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
        return M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[num%10];
