class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        found_numbers = {}
        for idx, number in enumerate(numbers):
            target_quotent = target - number
            if target_quotent in found_numbers and idx != found_numbers[target_quotent]:
                return [
                    found_numbers[target_quotent] + 1,
                    idx + 1,
                ]
            found_numbers[number] = idx
    
    def twoSumWithTwoPointers(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1

        # we know exactly where to shift the pointers because the array is sorted
        while (left < right):
            left_number = numbers[left]
            right_number = numbers[right]
            total = left_number + right_number
            if total == target:
                return [left + 1, right + 1]
            elif total > target:
                right -= 1
            else:
                left += 1
        
solution = Solution()
result = solution.twoSumWithTwoPointers([2,7,11,15], 9)
print(result)
result = solution.twoSumWithTwoPointers([2,3,4], 6)
print(result)
result = solution.twoSumWithTwoPointers([-1,0], -1)
print(result)
result = solution.twoSumWithTwoPointers([0,0,3,4], 0)
print(result)