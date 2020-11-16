"""
medium

给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

grid = [
[1,3,1],
[1,5,1],
[4,2,1
]
分析：
1. 状态定义,i为横轴，j为纵轴
dp[i][j]的值代表走到(i,j)位置的最小路径和
2. 转移方程
    a.每次只能向下或者向右移动一步，说明当前元素只能从上(i,j-1)或者从左边(i-1,j)过来
    b.走到当前单元格 (i,j)(i,j) 的最小路径和 == “从左方单元格 (i-1,j)(i−1,j) 与 从上方单元格 (i,j-1)(i,j−1) 走来的 两个最小路径和中较小的 ” ++ 当前单元格值 grid[i][j]grid[i][j] 。
    具体分为以下 4种情况：
        b1:i,j都为0 dp[i][j] = grid[i][j]
        b2:i=0,j≠0 dp[i][j] = dp[i][j-1]+grid[i][j]
        b3:i≠0,j=0 dp[i][j] = dp[i-1][j]+grid[i][j]
        b4:i≠0,j≠0 dp[i][j] = min(dp[i][j-1]+grid[i][j],dp[i-1][j]+grid[i][j]) +grid[i][j]
"""

grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]


def minPathSum(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == j == 0:
                continue
            elif i == 0:
                grid[i][j] = grid[i][j - 1] + grid[i][j]
            elif j == 0:
                grid[i][j] = grid[i - 1][j] + grid[i][j]
            else:
                grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
    return grid[-1][-1]


print(minPathSum(grid))