#初版：1100+ms
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s = sorted(s)
        tapg = 0
        taps = 0
        rtype = 0
        while tapg < len(g):
            for i in range(taps,len(s)): 
                if g[tapg] > s[taps]:
                    taps += 1
                    continue
                else:
                    taps += 1
                    rtype += 1
                    break
            tapg += 1
        return rtype
#看了别人的再写的：95ms
#尽量在能不用多重循环的时候不用多重循环
    class Solution(object):
        def findContentChildren(self, g, s):
            """
            :type g: List[int]
            :type s: List[int]
            :rtype: int
            """
            g = sorted(g)
            s = sorted(s)
            tapg = 0
            taps = 0
            rtype = 0
            while tapg < len(g) and taps < len(s):
                if g[tapg] <= s[taps]:
                    tapg += 1
                    taps += 1
                    rtype += 1
                else:
                    taps += 1
            return rtype