#最速答案
class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
        dict = ["a", "aa", "aaa", "aaaa"]
        sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
        rootDict = {}
        for root in dict:
            try:
                rootDict[root[0]].append(root)
                #增加键（注意，这个字典的键是列表，列表是一连串的root）
                print(rootDict)
            except:
                rootDict[root[0]] = [root]
        print(rootDict)
        sentenceList = sentence.split(' ')
        #sentence切割为列表
        for i in range(0, len(sentenceList)):
            word = sentenceList[i]
            if word[0] in rootDict:
                for root in rootDict[word[0]]:
                    if word.startswith(root):
                        sentenceList[i] = root
                        break
        print(" ".join(sentenceList))

#自己写的初版
class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        list_s = sentence.split(' ')
        rtype = []
        Flag = 0
        for w in list_s:
            for Dicw in dict:
                if Dicw in w[:len(Dicw)]:
                    rtype.append(Dicw)
                    Flag = 1
                    break
            if Flag == 0 :
                rtype.append(w)
            else:
                Flag = 0
        rtype = ' '.join(rtype)
        return rtype

#借鉴了66ms版答案写的2版
#借助了Start With
class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        list_s = sentence.split(' ')
        for i in range(0,len(list_s)):
            for Dicw in dict:
                if  list_s[i].startswith(Dicw):
                    list_s[i] = Dicw
        rtype = ' '.join(list_s)
        return rtype

#第三版，先对root别表按长度进行排序
class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        list_s = sentence.split(' ')
        dict.sort(key=lambda x:len(x))
        for i in range(0,len(list_s)):
            for Dicw in dict:
                if  list_s[i].startswith(Dicw):
                    list_s[i] = Dicw
                    break
        rtype = ' '.join(list_s)
        return rtype