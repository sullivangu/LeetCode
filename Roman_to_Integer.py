class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        lastValue = 0
        dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for c in reversed(s):
            if lastValue <= dict[c]:
                num += dict[c]
            else:
                num -= dict[c]
            lastValue = dict[c]
        return num

