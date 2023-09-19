"""
202. 快乐数

编写一个算法来判断一个数 n 是不是快乐数。

快乐数定义为：
- 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
- 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
- 如果这个过程 结果为 1，那么这个数就是快乐数。

如果 n 是 快乐数 就返回 true ；不是，则返回 false 。
"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        record = set()
        while n != 1:
            if n in record:
                return False
            else:
                record.add(n)
                n = self.update(n)
        return True

    def update(self, n):
        ans = 0
        while n!=0:
            ans += (n%10)**2
            n = n // 10
        return ans


if __name__ == '__main__':
    n = 19
    solu = Solution()
    print(solu.isHappy(n))  # True
