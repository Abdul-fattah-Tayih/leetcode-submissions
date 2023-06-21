from typing import List

class KRadiusSubarray:
    """
        2090. K Radius Subarray Averages

        You are given a 0-indexed array nums of n integers, and an integer k.

        The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums 
        between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.

        Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.

        The average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero, 
        which means losing its fractional part.

        For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.

        https://leetcode.com/problems/k-radius-subarray-averages/
    """
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        """
            O(2n) => O(n) solution

            Instead of going through the window in each iteration (takes O(n^2) time), we calculate prefix sum

            Which is an array that contains the sums of elements, and in each index is the total sum up until that index

            That helps us because in each iteration, the sum of the the k radius subarray is prefix sum of (i + k) - prefix sum of (i - k - 1)

            Let's break that down:
                for example we have this input: nums = [7,4,3,9,1,8,5,2,6], k = 3
                And we generated this prefix sum array: [7, 11, 14, 23, 24, 32, 37, 39, 45]
                1. Anything before index 3 is -1, because there are no k elements behind it (this is in problem statement)
                2. At index 3, my total sum is prefix_sum[3 + k] = prefix_sum[6] = 37
                3. And since index 0 is within the subarray, we don't need to deduct anything
                4. So result is 37 / 7 (k on each side so k * 2, plus the element in the middle so 3 * 2 + 1)
                5. In the next iteration the total is 39
                6. But we've moved the subarray one step, so index 0 is the last element outside of the subarray, so the result is 39 - prefix_sum[0]
                and so on
        """

        
        prefix_sum = []
        for i, num in enumerate(nums):
            if i > 0:
                prefix_sum.append(num + prefix_sum[i - 1])
            else:
                prefix_sum.append(num)

        left = 0
        result = []
        num_count = k * 2 + 1
        for right, num in enumerate(nums):
            if right - k < 0 or right + k >= len(nums):
                result.append(-1)
                continue

            subarray_sum = prefix_sum[right + k]

            if left > 0:
                subarray_sum -= prefix_sum[left - 1]

            result.append(subarray_sum // num_count)
            left += 1
        
        return result

if __name__ == '__main__':
    obj = KRadiusSubarray()
    print(obj.getAverages([7,4,3,9,1,8,5,2,6], 3))