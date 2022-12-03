from typing import List

class FourSumII:
    """
        454. 4Sum II

        Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples 
        
        (i, j, k, l) such that:

            0 <= i, j, k, l < n

            nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
    """
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        """
            O(n^2)

            formula is num1 + num2 + num3 + num4 = 0

            in this iteration we know num1 so

            num2 + num3 + num4 = -num1

            and num3 + num4 = -num1 - num2

            or num1 + num2 = - num3 - num4

            so we just need to find all combinations in any 2 sets

            and then we check the other 2

            https://leetcode.com/submissions/detail/853889683/
        """
        tuple_count = 0
        summation_dict = {}

        for num1 in nums1:
            for num2 in nums2:
                summation_dict[num1 + num2] = summation_dict.get(num1 + num2, 0) + 1

        for num3 in nums3:
            for num4 in nums4:
                tuple_count += summation_dict.get(-num3 - num4, 0)

        return tuple_count

    def four_sum_count_brute_force(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        """
            O(n ^ 4)

            This is very expensive and shouldn't be the solution, however, we can use this

            as a starting point and find ways to optimize it
        """
        tuple_count = 0

        for num1 in nums1:
            for num2 in nums2:
                for num3 in nums3:
                    for num4 in nums4:
                        if (num1 + num2 + num3 + num4) == 0:
                            tuple_count += 1
        return tuple_count

if __name__ == '__main__':
    obj = FourSumII()

    assert obj.fourSumCount(nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]) == 2
    assert obj.fourSumCount(nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]) == 1