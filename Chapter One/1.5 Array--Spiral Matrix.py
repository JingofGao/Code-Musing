"""
59. 螺旋矩阵 II

给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
输入: 3 输出: [ [ 1, 2, 3 ], [ 8, 9, 4 ], [ 7, 6, 5 ]
"""


def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    arr = [[0] * n for _ in range(n)]

    value = 1
    cur_row = 0
    cur_col = 0

    # 左闭右开
    for _ in range(n // 2):
        # 从左往右
        for j in range(cur_col, n - cur_col - 1):
            arr[cur_row][j] = value
            value += 1
        cur_col = j + 1

        # 从上到下
        for i in range(cur_row, n - cur_row - 1):
            arr[i][cur_col] = value
            value += 1
        cur_row = i + 1

        # 从右往左
        for j in range(cur_col, n - cur_col - 1, -1):
            arr[cur_row][j] = value
            value += 1
        cur_col = j - 1

        # 从下往上
        for i in range(cur_row, n - cur_row - 1, -1):
            arr[i][cur_col] = value
            value += 1
        cur_row = i - 1

        # 改变出发点
        cur_row += 1
        cur_col += 1

    # 最后判断奇偶
    if n % 2 == 1:
        arr[cur_row][cur_col] = value
    return arr


if __name__ == '__main__':
    n = 4
    arr = generateMatrix(n)
    print(arr)
