"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

"""
# 思路：栈+哈希表

s = "{[()]}"


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    # 字典结构左括号为key，右括号为value
    dict = {"(": ")", "{": "}", "[": "]"}
    stack = ["?"]
    for i in s:
        # 当遇到左括号时入栈
        if i in dict:
            stack.append(i)
        # 当遇到右括号时，判断栈的最后一个元素是不是与之匹配的左括号，不是的话就返回False
        elif i != dict[stack.pop()]:
            return False
    return len(stack) == 1


print(isValid(s))
