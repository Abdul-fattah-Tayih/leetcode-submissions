class Solution:
    def min_partitions(self, n: str) -> int:
        """
            The minimum number of partitions is equals to the largest digit in the number
            for example, if we had the number 519, the result is equals to = 111 + 101 + 101 + 101 + 101 + 1 + 1 + 1 + 1
            O(n)
        """
        max_digit = 0
        for digit in n:
            digit = int(digit)
            max_digit = max(max_digit, digit)
            if max_digit == 9: return 9 # early exit because a decimal digit max is 9 (improves speed from 5% faster to 20% faster)

        return max_digit

    def min_partitions_brute_force(self, n: str) -> int:
        """
            Find the actual numbers to add, O(n^2)
            fails on leetcode because of time limit
        """
        numbers_to_add = []
        for idx, digit in enumerate(n):
            digit = int(digit)
            for i in range(digit):
                if i < len(numbers_to_add):
                    numbers_to_add[i] = numbers_to_add[i][:idx] + '1' + numbers_to_add[i][idx + 1:]
                else:
                    numbers_to_add.append(f'{"0" * idx}1{"0" * (len(n) - 1 - idx)}')

        return len(numbers_to_add)

solution = Solution()
print(f'should be: 3, actual {solution.min_partitions("32")}')
print(f'should be: 8, actual {solution.min_partitions("82734")}')
print(f'should be: 9, actual {solution.min_partitions("27346209830709182346")}')