from typing import List, Set, Tuple, Dict

class PermutationsII:
    """
        47. Permutations II

        Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
    """
    def permuteUniqueSet(self, nums: List[int]) -> List[List[int]]:
        result_set = self.permute_unique_recursively_with_set(len(nums), nums, [], set())

        result = []
        for permutation in result_set:
            result.append(list(permutation))

        return result

    def permute_unique_recursively_with_set(self, permutation_length: int, remaining_numbers: List[int], current_permutation: List[int], permutations: Set[Tuple[int]]) -> Set[Tuple[int]]:
        """
            same as 46, but we use a set of tuples to avoid inserting duplicates

            The reason for that is:
                1. Sets contain unique items, so if an existing item is about to be inserted, then it won't be added again
                2. Tuples are hashable and can work with sets and dictionary keys, if we try to use a list, it will raise an exception

            https://leetcode.com/problems/permutations-ii/submissions/863889580/
        """
        if len(current_permutation) == permutation_length:
            permutations.add(tuple(current_permutation))
            return permutations

        for index, num in enumerate(remaining_numbers):
            remaining_numbers_except_num = remaining_numbers.copy()
            remaining_numbers_except_num.pop(index)
            self.permute_unique_recursively_with_set(permutation_length, remaining_numbers_except_num, current_permutation + [num], permutations)

        return permutations

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        frequency_dict = {}
        for num in nums:
            frequency_dict[num] = frequency_dict.get(num, 0) + 1

        return self.permute_unique_recursively_with_frequency_dict(len(nums), frequency_dict, [], [])

    def permute_unique_recursively_with_frequency_dict(self, permutation_length: int, remaining_numbers: Dict[int, int], current_permutation: List[int], permutations: List[List[int]]) -> List[List[int]]:
        """
            Instead of using the remaining numbers as an array, we use a frequency dict, so in each loop in our backtracking
            
            we actually go over each unique element once

            https://leetcode.com/problems/permutations-ii/submissions/863898505/
        """
        if len(current_permutation) == permutation_length:
            permutations.append(current_permutation)
            return permutations

        for num, count in remaining_numbers.items():
            remaining_numbers_minus_current = remaining_numbers.copy()
            remaining_numbers_minus_current[num] -= 1
            if remaining_numbers_minus_current[num] <= 0:
                del remaining_numbers_minus_current[num]

            self.permute_unique_recursively_with_frequency_dict(permutation_length, remaining_numbers_minus_current, current_permutation + [num], permutations)

        return permutations


if __name__ == '__main__':
    obj = PermutationsII()

    assert obj.permuteUnique([1,1,2]).sort() == [[1,1,2],[1,2,1],[2,1,1]].sort()
    assert obj.permuteUnique([1,2,3]).sort() == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].sort()