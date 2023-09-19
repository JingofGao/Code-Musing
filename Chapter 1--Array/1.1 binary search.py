"""
704. 二分查找

给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target ，
写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
"""


# 解法一：左闭右闭区间
def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    ans = -1

    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            ans = mid
            break
    return ans


# 解法二：左闭右开区间
# def search(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: int
#     """
#     ans = -1
#
#     low = 0
#     high = len(nums)
#     while low < high:
#         mid = (low + high) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] > target:
#             high = mid
#         elif nums[mid] < target:
#             low = mid + 1
#     return ans


if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    target = 9
    ans = search(nums, target)
    print(ans)  # 4
