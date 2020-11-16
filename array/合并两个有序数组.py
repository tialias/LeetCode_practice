"""

easy

1. 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

2. 说明：
初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

3. 示例：
输入：
nums1 = [1,2,3,0,0,0], m = 6
nums2 = [2,5,6],       n = 1

输出：[1,2,2,3,5,6]

1 2 2 3 5
"""
# 分析： 双指针

def merge(nums1, m, nums2, n):
    nums1_copy = nums1[:m]
    nums1[:] = []
    p1 = 0
    p2 = 0
    while p1 < m and p2 < n:
        if nums1_copy[p1] < nums2[p2]:
            nums1.append(nums1_copy[p1])
            p1 += 1
        else:
            nums1.append(nums2[p2])
            p2 += 1
    # 若此时p2>n,仍然要把nums1中的元素继续合并
    if p1 < m:
        nums1[p1 + p2 :] = nums1_copy[p1:]
    # 若此时p1 > m, 仍然要把nums2中的元素继续合并
    if p2 < n:
        nums1[p1 + p2 :] = nums2[p2:]
    return nums1


print(merge(
    [1, 2, 3, 0, 0, 0], 4, [2, 5, 6], 3,
))
