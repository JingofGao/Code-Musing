"""
344. 反转字符串

编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。
"""


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        low = 0
        high = len(s)-1
        while low<high:
            tmp = s[low]
            s[low] = s[high]
            s[high] = tmp

            low += 1
            high -= 1
        return s


if __name__ == '__main__':
    s = ["h","e","l","l","o"]
    solu = Solution()
    print(solu.reverseString(s))  # ['o', 'l', 'l', 'e', 'h']
