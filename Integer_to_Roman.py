class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        """
        Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
        """

        result = ''
        digit = int(num/1000)
        for i in range(digit):
            result += 'M'


        num -= digit*1000
        digit = int(num / 100)
        if digit == 9:
            result += 'CM'
        elif digit == 4:
            result += 'CD'
        elif digit == 5:
            result += 'D'
        elif digit < 5:
            for i in range(digit):
                result += 'C'
        elif digit > 5:
            result += 'D'
            for i in range(digit - 5):
                result += "C"

        num -= digit*100
        digit = int(num / 10)
        if digit == 9:
            result += 'XC'
        elif digit == 4:
            result += 'XL'
        elif digit == 5:
            result += 'L'
        elif digit < 5:
            for i in range(digit):
                result += 'X'
        elif digit > 5:
            result += 'L'
            for i in range(digit - 5):
                result += "X"

        num -= digit*10
        digit = int(num )
        if digit == 9:
            result += 'IX'
        elif digit == 4:
            result += 'IV'
        elif digit == 5:
            result += 'V'
        elif digit < 5:
            for i in range(digit):
                result += 'I'
        elif digit > 5:
            result += 'V'
            for i in range(digit - 5):
                result += "I"

        return result