class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard1 = 'QWERTYUIOPqwertyuiop'
        keyboard2 = 'ASDFGHJKLasdfghjkl'
        keyboard3 = 'ZXCVBNMzxcvbnm'
        Ans = []
        for word in words:
            Flag = 1
            InWhere = []
            for a in word:
                if a in keyboard1:
                    InWhere.append(1)
                elif a in keyboard2:
                    InWhere.append(2)
                elif a in keyboard3:
                    InWhere.append(3)
            InWhere = set(InWhere)
            if len(InWhere) != 1:
                Flag =0
            if Flag == 1:
                Ans.append(word)
        return Ans