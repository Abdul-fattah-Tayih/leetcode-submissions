from typing import List

class ContainsDuplicate:
    """
        217. Contains Duplicate

        Given an integer array nums, return true if any value appears at least twice in the array, 
        
        and return false if every element is distinct.
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
            O(n)

            We create a set of numbers, and while we are iterating, we check if a number

            exists in the set, if it does then we return True

            otherwise we return False after we finish iterating

            https://leetcode.com/submissions/detail/852236665/
        """
        nums_set = set()
        
        for num in nums:
            if num in nums_set:
                return True
            
            nums_set.add(num)
            
        return False