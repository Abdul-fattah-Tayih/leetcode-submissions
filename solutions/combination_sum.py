from typing import List, Set, Tuple
from utilities.lists import lists_contain_same_items

class CombinationSum:
    """
        39. Combination Sum

        Given an array of distinct integers candidates and a target integer target, 
        
        return a list of all unique combinations of candidates where the chosen numbers sum to target. 
        
        You may return the combinations in any order.

        The same number may be chosen from candidates an unlimited number of times. 
        
        Two combinations are unique if the frequency of at least one of the chosen numbers is different.

        The test cases are generated such that the number of unique combinations
        
        that sum up to target is less than 150 combinations for the given input.
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = self.combination_sum_recursive(candidates, target, set())

        result = list(result)
        result = map(lambda x: list(x), result)

        return list(result)

    def combination_sum_recursive(self, candidates: List[int], target: int, subsets: Set[Tuple[int]], i: int = 0, current_sum: int = 0, current_subset: List[int] = []) -> Set[Tuple[int]]:
        """
            Brute force solution

            Since we can use the same element unlimited times, then that means we have 3 recursive steps:
                1. Current element without moving in the list
                2. Sum Including current element
                3. Sum Excluding current element

            What we end up with is all possible subsets (including using an element multiple times)

            That add up to target, and our base cases are:
                1. i equals length of list
                2. sum equals target
                3. sum greater than target

            We're using a set of tuples to avoid inserting duplicate subsets, which is why this is a brute force solution

            https://leetcode.com/problems/combination-sum/submissions/864891849/
        """
        if i == len(candidates):
            if current_sum == target:
                subsets.add(tuple(current_subset))

            return subsets

        if current_sum == target:
            subsets.add(tuple(current_subset))
            return subsets

        if current_sum > target:
            return subsets

        # keep trying current element
        if current_sum + candidates[i] <= target:
            self.combination_sum_recursive(candidates, target, subsets, i, current_sum + candidates[i], current_subset + [candidates[i]])

        # include current element and move
        if current_sum + candidates[i] <= target:
            self.combination_sum_recursive(candidates, target, subsets, i + 1, current_sum + candidates[i], current_subset + [candidates[i]])

        # exclude current element and move
        self.combination_sum_recursive(candidates, target, subsets, i + 1, current_sum, current_subset)

        return subsets

if __name__ == '__main__':
    obj = CombinationSum()

    assert lists_contain_same_items(obj.combinationSum([2,3,6,7], 7), [[2,2,3],[7]])
    assert lists_contain_same_items(obj.combinationSum([2,3,5], 8), [[2,2,2,2],[2,3,3],[3,5]])