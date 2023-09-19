"""
27. 移除元素

给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
"""


# 双指针法：不同指针记录不同状态
def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    target = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[target] = nums[i]
            target += 1
    return nums, target


if __name__ == '__main__':
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    new_nums, new_len = removeElement(nums, val)
    print(new_nums[:new_len])  # [0, 1, 3, 0, 4]
