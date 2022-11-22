from typing import List

class NextGreaterElementII:
    """
        503. Next Greater Element II

        Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

        The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.
    """
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
            O(n)

            Same approach as Next Greater Element I, we use a monotonic stack

            But since we can have duplicates, we cant store indexes in a hash, instead we store a tuple in the stack

            that contains the number itself and its index, and whenever we come across a number that is higher than

            The top of the stack, we keep popping and we use the index in each tuple in the stack to update the greater element

            index, we need to keep in mind that circular values are possible, so we dont stop at the end of the array

            our loop stops if we go through the array more than 2 times, or if the number of processed indexes is equals to the

            length of the input array

            https://leetcode.com/submissions/detail/848267109/
        """
        next_greater_elements = [-1 for num in nums]
        processed_indexes = set()
        rounds = 1
        stack = []

        i = 0
        while len(processed_indexes) < len(nums) and rounds <= 2:
            num = nums[i]
            while stack and num > stack[-1][0]:
                value = stack.pop()
                index = value[1]
                next_greater_elements[index] = num
                processed_indexes.add(index)

            stack.append((num, i))
            
            if (i + 1) >= len(nums):
                i = 0
                rounds += 1
            else:
                i += 1

        return next_greater_elements

    def next_greater_elements_optimized(self, nums: List[int]) -> List[int]:
        """
            O(n)

            Essentially the same approach as above, however we only store indexes in the stack

            and we loop over the array exactly twice

            i % len(nums) is to handle cases where i is greater than the length of the array, and it will return

            the correct index even after we pass the length of the array

            https://leetcode.com/submissions/detail/848271658/
        """
        next_greater_elements = [-1 for num in nums]
        stack = []

        for i in range(len(nums) * 2):
            num = nums[i % len(nums)]
            while stack and num > nums[stack[-1]]:
                next_greater_elements[stack.pop()] = num

            stack.append(i % len(nums))

        return next_greater_elements

if __name__ == '__main__':
    obj = NextGreaterElementII()

    assert obj.next_greater_elements_optimized([1,2,1]) == [2, -1, 2]
    assert obj.next_greater_elements_optimized([1,2,3,4,3]) == [2,3,4,-1,4]
