def smallest_missing_positive_integer(nums):
    i = 0
    while i < len(nums):
        num = nums[i]
        if num < len(nums) and num > 0 and num - 1 != i:
            nums[num], nums[i] = nums[i], nums[num]
        else:
            i += 1

    for i, num in enumerate(nums):
        if num - 1 != i and num > 0:
            return i

    return 1

smallest_missing_positive_integer([1,2,3,5])