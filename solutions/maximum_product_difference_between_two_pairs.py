from typing import List

"""
Question number 1913
Maximum Product Difference Between Two Pairs
O(n)
"""
class MaxProductDifference:
    def maxProductDifference(self, nums: List[int]) -> int:
        maximum_index = minimum_index = None
        maximum = second_maximum = 0
        minimum = second_minimum = 10 ** 4

        # first loop to find the min and max and their indices        
        for idx, num in enumerate(nums):
            if num > maximum:
                maximum = num
                maximum_index = idx

            if num < minimum:
                minimum = num
                minimum_index = idx

        # second loop to find the 2nd min and max according to the found indices
        for idx, num in enumerate(nums):
            if num <= maximum and num > second_maximum and idx != maximum_index:
                second_maximum = num

            if num >= minimum and num < second_minimum and idx != minimum_index:
                second_minimum = num
            
        
        return (maximum * second_maximum) - (minimum * second_minimum)
    
if __name__ == '__main__':
    object = MaxProductDifference()

    test_cases = [
        ([5,6,2,7,4], 34),
        ([4,2,5,9,7,4,8], 64),
        ([10,10,10,10], 0)
    ]
    
    for idx, test_case in enumerate(test_cases):
        result = object.maxProductDifference(test_case[0])

        print(f"case {idx + 1} returned {result}, expected: {test_case[1]}")