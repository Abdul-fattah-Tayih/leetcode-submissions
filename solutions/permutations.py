from typing import List

class Permutations:
    """
        46. Permutations

        Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
            O()

            We're using recursive backtracking, to explain what's going on, let's draw a decision tree:

                          -----------[1, 2, 3]-----------
                         ↓               ↓               ↓
                      -[2,3]-         -[1,3]-         -[1,2]-
                     ↓       ↓       ↓       ↓       ↓       ↓
                    [3]     [2]     [3]     [1]     [1]     [2]

            To find all the possible permutations, we have to remove an element from the nums array

            And in each iteration, and then we try to add the remaining elements in another recursive iteration

            Once we reach a permutation list of length == length of nums, then we stop the recursion

            This will make us go back a step and try the next remaining number and so on
        
            https://leetcode.com/problems/permutations/submissions/863852825/
        """
        return self.permute_recursive(len(nums), nums, [], [])

    def permute_recursive(self, permutation_length: int, remaining_nums: List[int], current_permutation: List[int], permuatations: List[List[int]]) -> List[List[int]]:
        if len(current_permutation) == permutation_length:
            permuatations.append(current_permutation)
            return permuatations

        for index, num in enumerate(remaining_nums):
            new_remaining_nums = remaining_nums.copy()
            new_remaining_nums.pop(index)
            self.permute_recursive(permutation_length, new_remaining_nums, current_permutation + [num], permuatations)

        return permuatations

if __name__ == '__main__':
    obj = Permutations()

    assert obj.permute([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]