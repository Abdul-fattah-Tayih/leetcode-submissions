from typing import List

class MissingNumber:
    """
        268. Missing Number

        Given an array nums containing n distinct numbers in the range [0, n]
        
        return the only number in the range that is missing from the array.
    """
    def missingNumber(self, nums: List[int]) -> int:
        """
            O(n)

            Store all numbers in a set, then we look for all numbers

            in the range [0, len(nums) + 1], and if we don't find an element in the set

            then that element is missing

            https://leetcode.com/submissions/detail/852948040/
        """
        numbers_set = set(nums)

        for num in range(len(nums) + 1):
            if num not in numbers_set:
                return num
            
        return -1