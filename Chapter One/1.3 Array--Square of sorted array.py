"""
977. 有序数组的平方

给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
"""


# 双指针法
def sortedSquares(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    low = 0
    high = len(nums) - 1

    ans = [0] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        if nums[low] ** 2 > nums[high] ** 2:
            ans[i] = nums[low] ** 2
            low += 1
        else:
            ans[i] = nums[high] ** 2
            high -= 1

    return ans


if __name__ == '__main__':
    nums = [-4, -1, 0, 3, 10]
    ans = sortedSquares(nums)
    print(ans)  # [0, 1, 9, 16, 100]
