from typing import List

class ContainerWithMostWater:
    """
    Question 11

    Container with most water

    You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container, such that the container contains the most water.

    Return the maximum amount of water a container can store.

    Notice that you may not slant the container.
    """
    def maxArea(self, height: List[int]) -> int:
        """
            The idea here is to use 2 pointers, one at each end of the array
            Then we calculate the area of the columns that are at each pointer
            and compare it to the max area, and then move the pointer that points
            to the lower height

            O(n)
        """
        left = 0
        right = len(height) - 1

        max_area = -10 ** 4
        while left < right:
            left_height = height[left]
            right_height = height[right]
            area = min(left_height, right_height) * (right - left)
            max_area = max(area, max_area)

            if left_height > right_height:
                right -= 1
            else:
                left += 1

        return max_area

if __name__ == '__main__':
    object = ContainerWithMostWater()
    print(object.maxArea([1,8,6,2,5,4,8,3,7]))
    print(object.maxArea([1,1]))
            