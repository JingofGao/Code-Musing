"""
151. 反转字符串中的单词

给你一个字符串 s ，请你反转字符串中 单词 的顺序。

单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。

返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。

注意：输入字符串 s中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，
单词间应当仅用单个空格分隔，且不包含任何额外的空格。
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)

        # 1.删除多余空格
        ind = 0
        space_num = 0
        for i in range(len(s)):
            if s[i] == " ":
                space_num += 1
                if space_num <= 1:
                    s[ind] = s[i]
                    ind += 1
            else:
                space_num = 0
                s[ind] = s[i]
                ind += 1

        low = 0
        high = ind
        if s[low] == " ":
            low += 1
        if s[high - 1] == " ":
            high -= 1

        s = s[low:high]

        # 2.将整个字符串反转
        s = self.reverseList(s)

        # 3.将每个单词反转回来
        low, high = 0, 0
        for i in range(len(s)):
            if s[i] != " ":
                high += 1
            else:
                s[low:high] = self.reverseList(s[low:high])
                low, high = i + 1, i + 1
        s[low:high] = self.reverseList(s[low:high])

        return "".join(s)

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
    s = "We are happy"
    solu = Solution()
    print(solu.reverseWords(s))  # "happy are We"
