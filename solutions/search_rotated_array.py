from typing import List

class SearchInARotatedArray:
    """
        33. Search in Rotated Sorted Array

        There is an integer array nums sorted in ascending order (with distinct values).

        Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k 
        
        (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
        
        For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

        Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

        You must write an algorithm with O(log n) runtime complexity.
    """
    def search(self, nums: List[int], target: int) -> int:
        """
            O(n log(n))

            Our solution is to binary search the array, but with a few conditions, we initially assign a middle and then check it

            against our target, we make an assumption about which sorted portion we're at, so we compare mid to left

            If left <= mid, then that means we're in the left side of the array which is sorted, and so we can check if:

            1. target > mid or target < left: then we search in the right, because the left portion is sorted and the target is not between left and right of it
            2. target is between left and mid, in that case, we search in the left portion of the array

            else:
            
            1. target < mid or target > right: then we search in the left, because the right portion is sorted and the target is not between left and right of it
            2. target is between mid and right, in that case, we search in the right portion of the array
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if target < nums[left] or target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target > nums[right] or target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1

if __name__ == '__main__':
    obj = SearchInARotatedArray()

    assert obj.search(nums = [4,5,6,7,0,1,2], target = 0) == 4
    assert obj.search(nums = [4,5,6,7,0,1,2], target = 3) == -1
    assert obj.search([4,5,6,7,8,1,2,3], 8) == 4
    