from typing import List

class TrappingRainWater:
    """
        42. Trapping Rain Water

        Given n non-negative integers representing an elevation map where the width of each bar is 1, 
        
        compute how much water it can trap after raining.
    """
    def trap(self, heights: List[int]) -> int:
        """
            O(n) 2 pointer solution:

            The idea here is to put 2 pointers on both ends of the array

            Then we initialize the max of each side to the values of elements at both pointers

            In each iteration, we compare the max of left and right, and move the pointer with the max value

            and add the max - height of current element to the result
        """
        if not heights:
            return 0

        left = 0
        right = len(heights) - 1
        left_max = heights[left]
        right_max = heights[right]
        result = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, heights[left])
                result += (left_max - heights[left])
            else:
                right -= 1
                right_max = max(right_max, heights[right])
                result += (right_max - heights[right])

        return result

    def trap_stack(self, heights: List[int]) -> int:
        water_amount = 0
        stack = []

        for index, height in enumerate(heights):
            while stack and heights[stack[-1]] < height:
                bottom = heights[stack.pop()]
                if not stack:
                    break

                left = stack[-1]
                water_height = min(heights[left], height) - bottom
                water_width = index - left - 1

                water_amount += (water_height * water_width)

            stack.append(index)
        
        return water_amount

if __name__ == '__main__':
    obj = TrappingRainWater()

    assert obj.trap_stack([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert obj.trap_stack([4,2,0,3,2,5]) == 9