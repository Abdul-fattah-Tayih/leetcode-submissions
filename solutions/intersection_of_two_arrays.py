from typing import List

"""
Question number 349
Intersection of Two Array
O(n)
"""
class IntersectionOfTwoArrays:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        intersection_set = set()

        for num in nums2:
            if num in nums1_set:
                intersection_set.add(num)

        return list(intersection_set)