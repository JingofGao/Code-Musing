"""
541. 反转字符串 II

给定一个字符串 s 和一个整数 k，从字符串开头算起，每计数至 2k 个字符，就反转这 2k 字符中的前 k 个字符。
- 如果剩余字符少于 k 个，则将剩余字符全部反转。
- 如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
"""


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)

        i = 0
        while i < len(s):
            s[i:i + k] = self.reverseList(s[i:i + k])
            i += 2 * k
        s[i:i + k] = self.reverseList(s[i:i + k])

        return ''.join(s)  # list -> str

    def reverseList(self, s):
        low = 0
        high = len(s) - 1
        while low < high:
            tmp = s[low]
            s[low] = s[high]
            s[high] = tmp

            low += 1
            high -= 1
        return s


if __name__ == '__main__':
    s = "abcdefg"
    k = 2
    solu = Solution()
    print(solu.reverseStr(s,k))  # "bacdfeg"
