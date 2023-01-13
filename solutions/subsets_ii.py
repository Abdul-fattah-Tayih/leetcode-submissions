from typing import List
from utilities.lists import lists_contain_same_items

class SubsetsII:
    """
        90. Subsets II

        Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

        The solution set must not contain duplicate subsets. Return the solution in any order.
    """
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 1:
            return []

        nums.sort()

        return self.get_subsets_recursive(nums, 0, [], [])

    def get_subsets_recursive(self, nums: List[int], i: int, current_subset: List[int], subsets: List[List[int]]) -> List[List[int]]:
        """
            Recursive backtracking, what we do in these kinds of problems is to iterate over the list

            However, the difference here is that the input isn't always unique, which will cause duplicates

            So we use the list itself, but we sort it so we can skip all duplicate values when needed,
            
            And as we move we attempt adding a subset

            while either:
                1. including the element at the current index
                2. excluding the element at the current index

            We keep doing that until i is equals to the length of the list, in that case we stop and return

            When we return it will backtrack to the previous step and then try excluding instead

            of including or vice versa 

            https://leetcode.com/problems/subsets-ii/submissions/864829568/
        """
        if len(nums) == i:
            subsets.append(current_subset)
            return subsets

        self.get_subsets_recursive(nums, i + 1, current_subset + [nums[i]], subsets)

        while i + 1< len(nums) and nums[i] == nums[i + 1]:
            i += 1

        self.get_subsets_recursive(nums, i + 1, current_subset, subsets)

        return subsets


if __name__ == '__main__':
    obj = SubsetsII()

    assert lists_contain_same_items(obj.subsetsWithDup([1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
    assert lists_contain_same_items(obj.subsetsWithDup([1,2,2]), [[],[1],[1,2],[1,2,2],[2],[2,2]])
