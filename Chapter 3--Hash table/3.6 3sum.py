"""
15. 三数之和

给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，
同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        target = 0

        # 先对nums排序
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > target:
                return ans

            # 去重i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            low = i + 1
            high = len(nums) - 1
            while low < high:
                if nums[i] + nums[low] + nums[high] > target:
                    high -= 1
                elif nums[i] + nums[low] + nums[high] < target:
                    low += 1
                else:
                    ans.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1

                    # 去重j,k
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1
        return ans


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    solu = Solution()
    print(solu.threeSum(nums))  # [[-1, -1, 2], [-1, 0, 1]]
