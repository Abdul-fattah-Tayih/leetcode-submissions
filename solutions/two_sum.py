from typing import List

class TwoSum:
    """
        1. Two Sum

        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

        You may assume that each input would have exactly one solution, and you may not use the same element twice.

        You can return the answer in any order.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
            Time: O(n)

            Space: O(n)

            We use a hash map to store all values as the keys and their indices as the values

            Then we iterate over the list and in each iteration we check the if the difference between the current

            number and the target exists in the hash map, making sure not to use the same element twice

            https://leetcode.com/submissions/detail/851187347/
        """
        # set the size at the start if possible to avoid o(n^2) due to copying
        number_indices = {value: index for index, value in enumerate(nums)}
        
        for index, num in enumerate(nums):
            required_number = target - num
            
            if required_number in number_indices and index != number_indices[required_number]:
                return [index, number_indices[required_number]]
            
        return []

if __name__ == '__main__':
    obj = TwoSum()

    assert obj.twoSum([2,7,11,15], 9) == [0, 1]
    assert obj.twoSum([3,2,4], 6) == [1, 2]
    assert obj.twoSum([3,3], 6) == [0, 1]