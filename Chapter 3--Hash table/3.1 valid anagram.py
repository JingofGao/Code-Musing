"""
242. 有效的字母异位词

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        record_s = [0] * 26
        record_t = [0] * 26

        for i in range(len(s)):
            record_s[ord(s[i]) - ord("a")] += 1
            record_t[ord(t[i]) - ord("a")] += 1

        for j in range(len(record_s)):
            if record_s[j] != record_t[j]:
                return False
        else:
            return True


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    solu = Solution()
    print(solu.isAnagram(s, t))  # True
