

"""
思路：哈希表+循环判断

"""


def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    m = 0
    for i in range(len(s) - 1):
        if dict.get(s[i]) < dict.get(s[i + 1]):
            m -= dict.get(s[i])
        else:
            m = m + dict.get(s[i])
    return m
