"""
20. 有效的括号

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
1.左括号必须用相同类型的右括号闭合。
2.左括号必须以正确的顺序闭合。
3.每个右括号都有一个对应的相同类型的左括号。
"""


# 一、遇到左括号，入栈
# 二、遇到右括号，出栈，是否匹配
# 1.出栈返回空，return False
# 2.出栈的左括号不等于右括号，return False
# 三、遍历结束再次判断
# 1.栈不为空，return False
# 2.栈为空，return True

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for ele in s:
            if ele in ["(", "{", "["]:
                stack.append(ele)
            else:
                if not stack or stack.pop()+ele not in ["()", "{}", "[]"]:
                    return False
        if stack:
            return False
        else:
            return True


if __name__ == '__main__':
    s = "()[]{}"
    solu = Solution()
    print(solu.isValid(s))  # True
