from typing import List

class FindTheMiddleIndexInArray:
    """
        1991. Find the Middle Index in Array

        Given a 0-indexed integer array nums, find the leftmost middleIndex (i.e., the smallest amongst all the possible ones).

        A middleIndex is an index where nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].

        If middleIndex == 0, the left side sum is considered to be 0. Similarly, if middleIndex == nums.length - 1, the right side sum is considered to be 0.

        Return the leftmost middleIndex that satisfies the condition, or -1 if there is no such index.
    """
    def findMiddleIndex(self, nums: List[int]) -> int:
        """
            O(n)

            We calculate the sum of the entire list, 
            
            then in each iteration we modify each side based on the current element

            once we reach the point in-which we have left side == right side, we return the index

            if we exit the loop, then we know no middle index exists, and thus return -1
        """
        nums_sum = sum(nums)
        right_sum = nums_sum
        left_sum = 0

        for idx, num in enumerate(nums):
            if idx == 0:
                left_sum = 0
                right_sum -= num
            elif (idx + 1) == len(nums):
                right_sum = 0
                left_sum = (nums_sum - num)
            else:
                left_sum += nums[idx - 1]
                right_sum -= num

            if left_sum == right_sum:
                return idx

        return -1

if __name__ == '__main__':
    obj = FindTheMiddleIndexInArray()

    assert obj.findMiddleIndex([2,3,-1,8,4]) == 3
    assert obj.findMiddleIndex([1,-1,4]) == 2
    assert obj.findMiddleIndex([2,5]) == -1