from typing import List

class ContinuousSubarraySum:
    """
        523. Continuous Subarray Sum

        Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

        A good subarray is a subarray where:

        its length is at least two, and
        the sum of the elements of the subarray is a multiple of k.
        Note that:

        A subarray is a contiguous part of the array.
        An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
    """
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = { 0: -1 }
        total = 0

        for i, n in enumerate(nums):
            total += n
            r = total % k
            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] > 1:
                return True

        return False

    def check_subarray_sum_brute_force(self, nums: List[int], k: int) -> bool:
        """
            O(n^2), check all number combinations, times out in leetcode
        """
        for idx, num in enumerate(nums):
            sum = num
            for next_num_index in range(idx + 1, len(nums)):
                sum += nums[next_num_index]

                if self.is_multiple(sum, k):
                    return True

        return False


    def is_multiple(self, number, multiple_of) -> bool:
        result = number / multiple_of

        return int(result) == result

if __name__ == '__main__':
    obj = ContinuousSubarraySum()

    assert obj.checkSubarraySum([23,2,4,6,7], 6) == True
    assert obj.checkSubarraySum([23,2,6,4,7], 13) == False
    assert obj.checkSubarraySum([23,2,4,6,6], 7) == True
    assert obj.checkSubarraySum([5,0,0,0], 3) == True
    assert obj.checkSubarraySum([1,3,6,0,9,6,9], 7) == True