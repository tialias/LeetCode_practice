def midSelect(nums, key):
    nums = sorted(nums)
    print(nums)
    mid = len(nums) // 2
    if nums[mid] > key:
        return midSelect(nums[0:mid], key)
    elif nums[mid] < key:
        return midSelect(nums[mid + 1:], key)
    else:
        return mid


print(midSelect([1, 19, 5, 2, 20, 13], 19))
