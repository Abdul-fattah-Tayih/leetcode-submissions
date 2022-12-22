from typing import List

class Subsets:
    """
        78. Subsets

        Given an integer array nums of unique elements, return all possible subsets (the power set).

        The solution set must not contain duplicate subsets. Return the solution in any order.
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 1:
            return []

        return self.get_subsets_recursive(nums, 0, [], [])

    def get_subsets_recursive(self, nums: List[int], i: int, current_subset: List[int], subsets: List[List[int]]) -> List[List[int]]:
        """
            Recursive backtracking, what we do in these kinds of problems is to iterate over the list

            Keeping the current index stored, and in each iteration we recursively go deeper into the array

            while either:
                1. including the element at the current index
                2. excluding the element at the current index

            we keep doing that until the index is equal to the length of the array, in that case, we'll append the current

            subset to the result, and return, when we return it will backtrack to the previous step and then try excluding instead

            of including or vice versa 

            https://leetcode.com/problems/subsets/submissions/863935828/
        """
        if i == len(nums):
            subsets.append(current_subset)
            return subsets

        self.get_subsets_recursive(nums, i + 1, current_subset + [nums[i]], subsets)
        self.get_subsets_recursive(nums, i + 1, current_subset, subsets)

        return subsets


if __name__ == '__main__':
    obj = Subsets()

    assert obj.subsets([1,2,3]).sort() == [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]].sort()
