"""
1. 两数之和

给定一个整数数组 nums 和一个整数目标值 target，
请你在该数组中找出 和为目标值 target  的那两个整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        record = set()
        for i in range(len(nums)):
            if target-nums[i] in record:
                return [nums.index(target-nums[i]), i]
            else:
                record.add(nums[i])


if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    solu = Solution()
    print(solu.twoSum(nums, target))  # [0, 1]
