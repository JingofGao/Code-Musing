"""
454. 四数相加 II

给你四个整数数组 nums1、nums2、nums3 和 nums4 ，数组长度都是 n ，请你计算有多少个元组 (i, j, k, l) 能满足：
- 0 <= i, j, k, l < n
- nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
"""


class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        ans = 0
        record = dict()
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] + nums2[j] not in record:
                    record[nums1[i] + nums2[j]] = 1
                else:
                    record[nums1[i] + nums2[j]] += 1

        for i in range(len(nums3)):
            for j in range(len(nums4)):
                if 0 - nums3[i] - nums4[j] in record:
                    ans += record[0 - nums3[i] - nums4[j]]

        return ans


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [-2, -1]
    nums3 = [-1, 2]
    nums4 = [0, 2]

    solu = Solution()
    print(solu.fourSumCount(nums1, nums2, nums3, nums4))  # 2
