"""
349. 两个数组的交集

给定两个数组 nums1 和 nums2 ，返回 它们的交集 。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。
"""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        record1 = [0] * 1001
        record2 = [0] * 1001

        for ele in nums1:
            record1[ele] += 1
        for ele in nums2:
            record2[ele] += 1

        for i in range(1001):
            if record1[i] * record2[i] > 0:
                ans.append(i)
        return ans


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    solu = Solution()
    print(solu.intersection(nums1, nums2))  # [2]
