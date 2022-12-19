from typing import List

class SumOfAllSubsetXORTotals:
    """
        1863. Sum of All Subset XOR Totals

        The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

        * For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.

        Given an array nums, return the sum of all XOR totals for every subset of nums. 

        Note: Subsets with the same elements should be counted multiple times.

        An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.
    """
    def subsetXORSum(self, nums: List[int]) -> int:
        """
            O(2^n)

            Recursive backtracking

            The idea here is to create every possible subset for the list, to do that

            We keep iterating over the array, and in each time, we calculate the xor either 
            
            including or excluding the current element, then we stop at the end of the array

            And we add both values (including and excluding) for all the steps, and in the final step we will have the sums

            And we just add them together

            To do a bitwise XOR we use the `^` operator
        """
        if len(nums) == 0:
            return 0

        return self.subset_xor_sum_recursive(nums, 0, 0)

    def subset_xor_sum_recursive(self, nums: List[int], level: int, current_xor: int) -> int:
        if level == len(nums):
            return current_xor

        subset_sum_inclusive = self.subset_xor_sum_recursive(nums, level + 1, current_xor ^ nums[level])
        subset_sum_exclusive = self.subset_xor_sum_recursive(nums, level + 1, current_xor)

        return subset_sum_inclusive + subset_sum_exclusive

if __name__ == '__main__':
    obj = SumOfAllSubsetXORTotals()

    assert obj.subsetXORSum([1,3]) == 6
    assert obj.subsetXORSum([5,1,6]) == 28
    assert obj.subsetXORSum([3,4,5,6,7,8]) == 480