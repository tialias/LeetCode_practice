"""
medium
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""


def threeSum(nums):
    nums.sort()
    res, n = [], len(nums)
    # 小于3个元素，则没有
    if n < 3:
        return []
    for i in range(n):
        # 排好序的数组，若第一个元素大于0，则没有
        if nums[i] > 0:
            return res
        # 跳过与i重复的元素
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        L, R = i + 1, n - 1

        #循环终止条件
        while L < R:
            if nums[i] + nums[L] + nums[R] == 0:
                res.append([nums[i], nums[L], nums[R]])
                while L < R and nums[L] == nums[L + 1]:
                    L = L + 1
                while L < R and nums[R] == nums[R - 1]:
                    R = R - 1
                L, R = L + 1, R - 1
            elif nums[i] + nums[L] + nums[R] < 0:
                L += 1
            else:
                R -= 1
    return res


print(threeSum([0, 0, 0]))
