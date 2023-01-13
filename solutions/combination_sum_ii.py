from typing import List
from utilities.lists import lists_contain_same_items

class CombinationSumII:
    """
        40. Combination Sum II

        Given a collection of candidate numbers (candidates) and a target number (target), 
        
        find all unique combinations in candidates where the candidate numbers sum to target.

        Each number in candidates may only be used once in the combination.

        Note: The solution set must not contain duplicate combinations.
    """
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        return self.combination_sum_recursive(candidates, target, [])

    def combination_sum_recursive(self, candidates: List[int], target: int, subsets: List[List[int]], i: int = 0, current_sum: int = 0, current_subset: List[int] = []) -> List[List[int]]:
        """
            O(2^n)

            Recursive backtracking, in each recursive step, we try to move through the list by either:

                1. Including current element
                2. Excluding current element

            When we attempt to exclude current element, we keep moving the index if we find a duplicate element

            Until we reach a non duplicate, however while including we can include duplicates

            https://leetcode.com/problems/combination-sum-ii/submissions/864924826/
        """
        if i == len(candidates):
            if current_sum == target:
                subsets.append(current_subset)

            return subsets

        if current_sum == target:
            subsets.append(current_subset)
            return subsets

        if current_sum > target:
            return subsets

        # include current element and move
        if current_sum + candidates[i] <= target:
            self.combination_sum_recursive(candidates, target, subsets, i + 1, current_sum + candidates[i], current_subset + [candidates[i]])

        # move i until we find a non duplicate element
        while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
            i += 1

        # exclude current element and move
        self.combination_sum_recursive(candidates, target, subsets, i + 1, current_sum, current_subset)

        return subsets

if __name__ == '__main__':
    obj = CombinationSumII()

    assert lists_contain_same_items(obj.combinationSum2([10,1,2,7,6,1,5], 8), [[1,1,6],[1,2,5],[1,7],[2,6]])
    assert lists_contain_same_items(obj.combinationSum2([2,5,2,1,2], 5), [[1,2,2],[5]])