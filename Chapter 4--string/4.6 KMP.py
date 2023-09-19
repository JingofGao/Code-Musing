"""
28. 找出字符串中第一个匹配项的下标

给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。
如果 needle 不是 haystack 的一部分，则返回  -1 。
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        nx = self.get_nx(needle)

        i, j = 0, 0
        while i < len(haystack) and j < len(needle):
            if j < 0 or haystack[i] == needle[j]:
                # j<0表示出现了haystack[i]!=needle[0]
                i += 1
                j += 1
            else:
                j = nx[j]

        if j == len(needle):
            return i - j
        else:
            return -1

    def get_nx(self, s):
        nx = [-1] * len(s)
        t = -1
        i = 0
        while i < len(s) - 1:
            if t < 0 or s[i] == s[t]:
                i += 1
                t += 1
                nx[i] = t
            else:
                t = nx[t]
        return nx


if __name__ == '__main__':
    haystack = "leetcode"
    needle = "leeto"
    solu = Solution()
    print(solu.strStr(haystack, needle))  # 4
