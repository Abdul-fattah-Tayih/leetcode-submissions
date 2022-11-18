from typing import List

class MinimumSizeSubarraySum:
    """
        209. Minimum Size Subarray Sum

        Given an array of positive integers nums and a positive integer target, 
        
        return the minimal length of a subarray whose sum is greater than or equal to target. 
        
        If there is no such subarray, return 0 instead.
    """
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
            O(2n), we use a dynamic sliding window to find the shortest sub array that

            has a sum greater than or equal to target, if sum is >= target, then we move left

            otherwise we move right
        """
        min_sub_array_length = len(nums)
        found_min = False
        sum = 0
        last_added_index = None

        left = right = 0
        while left <= right and right < len(nums):
            if sum >= target:
                min_sub_array_length = min(min_sub_array_length, (right - left) + 1)
                found_min = True
                sum -= nums[left]
                left += 1
            else:
                if right != last_added_index:
                    sum += nums[right]
                    last_added_index = right

                if sum < target:
                    right += 1

        return min_sub_array_length if found_min else 0


if __name__ == '__main__':
    obj = MinimumSizeSubarraySum()

    assert obj.minSubArrayLen(7, [2,3,1,2,4,3]) == 2, f'minSubarrayLen for 7, [2,3,1,2,4,3] must return: 2, got {obj.minSubArrayLen(7, [2,3,1,2,4,3])}'
    assert obj.minSubArrayLen(4, [1,4,4]) == 1, f'minSubarrayLen for 4, [1,4,4] must return: 1, got {obj.minSubArrayLen(4, [1,4,4])}'
    assert obj.minSubArrayLen(11, [1,1,1,1,1,1,1,1]) == 0, f'minSubarrayLen for 11, [1,1,1,1,1,1,1,1] must return: 0, got {obj.minSubArrayLen(11, [1,1,1,1,1,1,1,1])}'