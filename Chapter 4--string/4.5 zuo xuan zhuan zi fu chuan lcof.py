"""
剑指 Offer 58 - II. 左旋转字符串

字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。
比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。
"""


class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        s = list(s)

        tmp = s[:n]
        ind = 0
        for i in range(n, len(s)):
            s[ind] = s[i]
            ind += 1
        for j in range(n):
            s[ind] = tmp[j]
            ind += 1

        return "".join(s)


if __name__ == '__main__':
    s = "abcdefg"
    k = 2
    solu = Solution()
    print(solu.reverseLeftWords(s,k))  # "cdefgab"
