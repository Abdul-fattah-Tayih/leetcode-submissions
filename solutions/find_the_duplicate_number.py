from typing import List

class FindTheDuplicateNumber:
    """
        287. Find the Duplicate Number

        Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

        There is only one repeated number in nums, return this repeated number.

        You must solve the problem without modifying the array nums and uses only constant extra space.
    """
    def find_duplicate(self, nums: List[int]) -> int:
        """
            O(n) Floyd's cycle detection

            https://leetcode.com/submissions/detail/852967790/
        """
        fast = slow = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow

    def find_duplicate_sort(self, nums: List[int]) -> int:
        """
            O(n log(n))

            This will submit, but the limitation of the question doesnt allow us to sort

            We sort the nums array, this will cause any duplicate numbers to be after each other

            Then we iterate over the sorted list, and compare the current number to the previous one

            If they match, then that's the duplicate number

            https://leetcode.com/submissions/detail/852959026/
        """
        nums = sorted(nums)
        for index, num in enumerate(nums):
            if index > 0 and nums[index - 1] == num:
                return num

        return -1