from typing import List

class FindMinimumInRotatedSortedArray:
    """
        153. Find Minimum in Rotated Sorted Array

        Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

        [4,5,6,7,0,1,2] if it was rotated 4 times.
        
        [0,1,2,4,5,6,7] if it was rotated 7 times.

        Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

        Given the sorted rotated array nums of unique elements, return the minimum element of this array.

        You must write an algorithm that runs in O(log n) time.

        Constraints:

        n == nums.length

        1 <= n <= 5000

        -5000 <= nums[i] <= 5000

        All the integers of nums are unique.

        nums is sorted and rotated between 1 and n times.
    """
    def findMin(self, nums: List[int]) -> int:
        """
            O(log(n))

            We don't know how many times this array was rotated, so we start with a normal binary search

            However in each iteration we check if the number on the left is greater than the one on the right

            This means that we are in a sorted section, which means we can get the minimum from the left number

            Otherwise, we check if our middle number is greater than the left number, in-which case, it means the minimum

            section of the array is on the right, otherwise we search the left side
        """
        left = 0
        right = len(nums) - 1

        minimum = 5000
        while left <= right:
            if nums[left] < nums[right]:
                minimum = min(minimum, nums[left])
                break

            mid = left + (right - left) // 2
            minimum = min(minimum, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return minimum


if __name__ == '__main__':
    obj = FindMinimumInRotatedSortedArray()

    assert obj.findMin([3,4,5,1,2]) == 1
    assert obj.findMin([4,5,6,7,0,1,2]) == 0
    assert obj.findMin([11,13,15,17]) == 11
    assert obj.findMin([5,1,2,3,4]) == 1