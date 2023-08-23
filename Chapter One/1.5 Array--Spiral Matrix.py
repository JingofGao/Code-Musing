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

    row = 0
    col = 0
    num = 1
    for _ in range(n // 2):
        # →
        for j in range(col, n - col - 1):
            arr[row][j] = num
            num += 1
        col = n - col - 1

        # ↓
        for i in range(row, n - row - 1):
            arr[i][col] = num
            num += 1
        row = n - row - 1

        # ←
        for j in range(col, n - col - 1, -1):
            arr[row][j] = num
            num += 1
        col = n - col - 1

        # ↑
        for i in range(row, n - row - 1, -1):
            arr[i][col] = num
            num += 1
        row = n - row - 1

        row += 1
        col += 1

    if n % 2 == 1:
        arr[row][col] = num
    return arr


if __name__ == '__main__':
    n = 4
    arr = generateMatrix(n)
    print(arr)
