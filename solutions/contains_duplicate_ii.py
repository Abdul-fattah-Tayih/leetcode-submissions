from typing import List

class ContainsDuplicateII:
    """
        219. Contains Duplicate II

        Given an integer array nums and an integer k, return true if there are two distinct indices i and j
        
        in the array such that nums[i] == nums[j] and abs(i - j) <= k.
    """
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
            O(n)

            We create a dict for the duplicates, and the value is the index

            While we loop over the nums, if we find the value again and the abs(current index - the index in the dict)

            are less than or equal to k, then return true, otherwise we return false after we finish iterating

            https://leetcode.com/submissions/detail/852257142/
        """
        duplicates_dict = {}

        for index, num in enumerate(nums):
            if num in duplicates_dict and abs(index - duplicates_dict[num]) <= k:
                return True

            duplicates_dict[num] = index

        return False


    def contains_nearby_duplicate_brute_force(self, nums: List[int], k: int) -> bool:
        """
            O(n^2)

            Create a dict of lists, each key in the dict represents a number

            and that number has a list of all indices that contain that number in the nums list

            We loop over nums again, and in each iteration we check if the difference between the indices

            is less than or equal to k

            https://leetcode.com/submissions/detail/852252970/
        """
        nums_dict = {}
        for index, num in enumerate(nums):
            if num in nums_dict:
                nums_dict[num].append(index)
            else:
                nums_dict[num] = [index]
        
        for index, num in enumerate(nums):
            for duplicate_index in nums_dict[num]:
                if duplicate_index != index and abs(duplicate_index - index) <= k:
                    return True
            
        return False

if __name__ == '__main__':
    obj = ContainsDuplicateII()

    assert obj.containsNearbyDuplicate(nums = [1,2,3,1], k = 3) == True
    assert obj.containsNearbyDuplicate(nums = [1,0,1,1], k = 1) == True
    assert obj.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2) == False
    assert obj.containsNearbyDuplicate([0,1,2,3,4,0,0,7,8,9,10,11,12,0], 1) == True