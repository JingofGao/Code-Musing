"""
剑指 Offer 05. 替换空格

请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
"""


class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 扩充维度
        ans = ["0"] * (len(s) * 3)

        ind = 0
        for ele in s:
            if ele != " ":
                ans[ind] = ele
                ind += 1
            else:
                ans[ind] = "%"
                ans[ind + 1] = "2"
                ans[ind + 2] = "0"
                ind += 3

        return "".join(ans[:ind])


if __name__ == '__main__':
    s = "We are happy."
    solu = Solution()
    print(solu.replaceSpace(s))  # "We%20are%20happy."
