from typing import List

class NextGreaterElementI:
    """
        496. Next Greater Element I

        The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

        You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

        For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

        Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
    """
    def next_greater_element(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
            O(n + m) Monotonically decreasing stack

            We store all elements of nums1 in a hash map that maps the number to the index

            Then, we loop over nums2, in each iteration we only add elements to the stack if they are in nums1

            and If we encounter an element that is greater than the top of the stack, we pop and store the popped number 

            In the results, and we keep going until the new greater number is in the stack, and we keep going

            The top of the stack indicates an element that is greater than all of the elements before it, so 

            When we pop, that means the top of the stack is greater than all previous numbers

            https://leetcode.com/submissions/detail/847508901/
        """
        next_greater_elements = [-1 for i in nums1]
        nums1_elements = {num: index for index, num in enumerate(nums1)}
        stack = []

        for i, num in enumerate(nums2):
            while stack and num > stack[-1]:
                value = stack.pop()
                index = nums1_elements[value]
                next_greater_elements[index] = num
            if num in nums1_elements:
                stack.append(num)

        return next_greater_elements
        

    def next_greater_element_brute_force(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
            O(n*m), store the indices of all nums2, then with each iteration in nums1

            we find the index of nums1[i] in nums2 and iterate to the end of the array until we find 

            a greater element, otherwise the value is -1

            https://leetcode.com/submissions/detail/847470983/
        """
        next_greater_elements = [-1 for i in nums1]
        nums2_elements = {}
        for idx, num in enumerate(nums2):
            if num not in nums2_elements:
                nums2_elements[num] = idx

        for idx, num in enumerate(nums1):
            index_in_nums2 = nums2_elements[num]
            for i in range(index_in_nums2, len(nums2)):
                num2 = nums2[i]
                if num2 > num:
                    next_greater_elements[idx] = num2
                    break

        return next_greater_elements

if __name__ == '__main__':
    obj = NextGreaterElementI()

    assert obj.next_greater_element(nums1 = [4,1,2], nums2 = [1,3,4,2]) == [-1,3,-1]
