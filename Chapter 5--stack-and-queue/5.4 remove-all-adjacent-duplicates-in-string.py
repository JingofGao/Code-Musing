"""
1047. 删除字符串中的所有相邻重复项

给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
在 S 上反复执行重复项删除操作，直到无法继续删除。
在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。
"""


class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for ele in s:
            if not stack:
                stack.append(ele)
                continue
            if stack[-1]== ele:
                stack.pop()
            else:
                stack.append(ele)
        return "".join(stack)


if __name__ == '__main__':
    s = "abbaca"
    solu = Solution()
    print(solu.removeDuplicates(s))  # ca
