#42ms
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(' ')
        ans = []
        for w in s:
            ans.append(w[::-1])
        return ' '.join(ans)

#35ms
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        for word in s.split():
            result.append(word[::-1])
        return " ".join(result)