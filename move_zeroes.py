class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        num_pointer = 0
        first_zero_pointer = None
        while num_pointer < len(nums):
            num = nums[num_pointer]
            if num == 0 and first_zero_pointer is None:
                first_zero_pointer = num_pointer
            elif num != 0 and first_zero_pointer is not None:
                temp = nums[num_pointer]
                nums[num_pointer] = 0
                nums[first_zero_pointer] = temp
                first_zero_pointer += 1

            num_pointer += 1
        print(nums)

    def moveZeroesExtraSpace(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        moved_array = []
        zero_count = 0
        for idx, num in enumerate(nums):
            if (num == 0):
                zero_count += 1
            else:
                moved_array.append(num)
                
        for i in range(zero_count):
            moved_array.append(0)
            
        nums = moved_array
        return moved_array

solution = Solution()
result = solution.moveZeroes([0,1,0,3,12])
result = solution.moveZeroes([0])
result = solution.moveZeroes([1,4,0,3,0])