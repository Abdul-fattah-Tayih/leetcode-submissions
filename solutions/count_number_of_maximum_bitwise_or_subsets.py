from typing import List


class CountNumberOfMaximumBitwiseOrSubsets:
    """
        2044. Count Number of Maximum Bitwise-OR Subsets

        Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.

        An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. Two subsets are considered different if the indices of the elements chosen are different.

        The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).
    """
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        """
            Recursive solution

            Time complexity: O(2^n)

            The maximum bitwise OR value is the bitwise OR of the entire array

            Then we check all possible subsets using recursion and backtracking by keeping a running bitwise_or value for each subset
            
            At the end of the subset, if it adds up to the maximum then it's an option, otherwise we stop the recursion
        """
        if not nums:
            return 0

        max_or = 0
        for num in nums:
            max_or = max_or | num

        result = 0
        def dfs(i, current_or):
            nonlocal max_or
            nonlocal result

            if i >= len(nums):
                if current_or == max_or:
                    result += 1

                return

            dfs(i + 1, current_or | nums[i])
            dfs(i + 1, current_or)

        dfs(0, 0)

        return result
    
if __name__ == "__main__":
    obj = CountNumberOfMaximumBitwiseOrSubsets()
    print(obj.countMaxOrSubsets([3,1]))
    print(obj.countMaxOrSubsets([2,2,2]))
    print(obj.countMaxOrSubsets([3,2,1,5]))