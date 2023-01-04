from typing import List, Set

class Combinations:
    """
        77. Combinations

        Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

        You may return the answer in any order.
    """
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums_set = set()
        for number in range(1, n + 1):
            nums_set.add(number)

        return self.combine_recursively(nums_set, k, [], [])

    def combine_recursively(self, remaining_numbers: Set[int], combination_length: int, current_combination: List[int], combinations: List[List[int]]) -> List[List[int]]:
        """
            Standard backtracking algorithm, but the twist is that we're not copying the remaining numbers in each iteration 

            Instead we remove an element once we're done to it, this is done to avoid duplicates ([2,1], and [1,2]), so a number will appear only

            In it's side of the tree.

            We use list(remaining_numbers) to avoid looping over the set while deleting from it which causes an exception

            https://leetcode.com/problems/combinations/submissions/863909903/
        """
        if len(current_combination) == combination_length:
            combinations.append(current_combination.copy())
            return combinations

        for number in list(remaining_numbers):
            # for efficiency, we avoid .copy() and + [list] as much possible, we do the result of that manually
            remaining_numbers.remove(number)
            current_combination.append(number)
            self.combine_recursively(remaining_numbers, combination_length, current_combination, combinations)
            current_combination.pop()
            remaining_numbers.add(number)

        return combinations

if __name__ == '__main__':
    obj = Combinations()

    assert obj.combine(4, 2) == [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    assert obj.combine(1, 1) == [[1]]