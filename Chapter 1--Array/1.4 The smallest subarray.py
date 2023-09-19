"""
209. 长度最小的子数组

给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。
如果不存在符合条件的子数组，返回 0。
"""


def minSubArrayLen(target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    ans = len(nums) + 1

    start = 0  # 起始位置
    sum_nums = 0

    # 遍历终止位置
    for i in range(len(nums)):
        sum_nums += nums[i]
        # 满足条件时，起始位置往后移
        while sum_nums >= target:
            ans = min(ans, i - start + 1)
            sum_nums -= nums[start]
            start += 1
    if ans == len(nums) + 1:
        return 0
    else:
        return ans


if __name__ == '__main__':
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    min_len = minSubArrayLen(target, nums)
    print(min_len)  # 2
