import math

"""
Question 231
Power of Two
"""
class PowerOfTwo:
    """
        O(n)
        Just loop over n, and find the power i each time and check against n
        Times out on leetcode...
    """
    def isPowerOfTwoGreedy(self, n: int) -> bool:
        if n != 1 and n % 2 != 0:
            return False

        for i in range(n):
            if 2 ** i == n:
                return True

        return False

    """
        O(1)
        This solution is bit manipulation
        Assume n = 8 (1000 in base 2), then n - 1 = 7 (0111 in base 2). 
        If you do a bitwise AND of these two, you get 0.
        This is true for n equal to any power of 2
    """
    def isPowerOfTwo(self, n: int) -> bool:
        return n != 0 and (n & (n - 1)) == 0

if __name__ == '__main__':
    object = PowerOfTwo()
    print(object.isPowerOfTwo(8))
    print(object.isPowerOfTwo(16))