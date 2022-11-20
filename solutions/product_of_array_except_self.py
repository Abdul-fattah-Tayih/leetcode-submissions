from typing import List

class ProductOfArrayExceptSelf:
    """
        238. Product of Array Except Self

        Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

        You must write an algorithm that runs in O(n) time and without using the division operation.
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
            O(n)

            If we were allowed to use division, we could have calculated the product of the entire list

            and in each iteration, we divided by the current element, but since we can't do that
            
            We can calculate prefix and postfix products, and in each iteration of the main list we multiply the prefix 
            
            at the previous position with the postfix at the next position and we'll have a solution
        """
        prefix_product = []
        for idx, num in enumerate(nums):
            if len(prefix_product) == 0:
                prefix_product.append(num)
            else:
                prefix_product.append(num * prefix_product[idx - 1])

        postfix_product = [1 for i in nums]
        for i in range(len(nums) - 1, -1, -1):
            if i == (len(nums) - 1):
                postfix_product[i] = nums[i]
            else:
                postfix_product[i] = nums[i] * postfix_product[i + 1]

        product_of_array = []
        for idx, num in enumerate(nums):
            if (idx - 1) < 0:
                prefix_value = 1
                postfix_value = postfix_product[idx + 1]
            elif (idx + 1 >= len(nums)):
                prefix_value = prefix_product[idx - 1]
                postfix_value = 1
            else:
                prefix_value = prefix_product[idx - 1]
                postfix_value = postfix_product[idx + 1]
            
            product_of_array.append(prefix_value * postfix_value)
        
        return product_of_array
            
if __name__ == '__main__':
    obj = ProductOfArrayExceptSelf()

    assert obj.productExceptSelf([1,2,3,4]) == [24,12,8,6]
    assert obj.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]