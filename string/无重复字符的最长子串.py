"""
1. 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        "pwkkew"
        """
        s1 = []  # 定义一个空列表，每次循环处理的最长子串都保存
        tmp = []  # 定义一个空列表， 保存每次循环的后的子串
        for i in s:
            if i not in tmp:
                tmp.append(i)
            else:
                index = tmp.index(i)
                tmp = tmp[(index + 1):]
                tmp.append(i)
            if len(tmp) > len(s1):
                s1 = tmp
        return s1


print(Solution().lengthOfLongestSubstring("abcabcdbb"))
