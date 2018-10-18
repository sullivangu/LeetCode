class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ""

        loopCount = len(strs[0])
        for s in strs:
            if len(s) < loopCount:
                loopCount = len(s)

        commonPrefix = ""
        end = False
        for i in range(loopCount):
            current = strs[0][i]
            if end == False:
                for s in strs:
                    if current != s[i]:
                        end = True
                        break
                if end == False:
                    commonPrefix += current
            else:
                break

        return commonPrefix
