from typing import List
from collections import deque

class SlidingWindowMaximum:
    """
        239. Sliding Window Maximum

        You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
        
        You can only see the k numbers in the window. Each time the sliding window moves right by one position.

        Return the max sliding window.
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
            O(n) monotonic decreasing double ended queue (deque)

            We append the index of elements in the queue if the values are less than the top of the queue (index -1)
            
            or the result of peek(), then once right reaches k we store the first item in the queue which is the greatest

            and then we increase left by 1, and in the next iteration, we compare the number with the top of the queue

            if its greater we keep popping until either the queue is empty or the top of the queue is greater than or equal than the number

            this will ensure that in each iteration we will have the greatest element's index in the window at the top, finally if 

            left is greater than the index of the first element in the queue, we remove that element from the queue, because that means

            that the window has shifted

            https://leetcode.com/submissions/detail/849628179/
        """
        result = []
        queue = deque()
        left = 0
        for right, num in enumerate(nums):
            while queue and nums[queue[-1]] < num:
                queue.pop()

            queue.append(right)

            if left > queue[0]:
                queue.popleft()

            if (right + 1) >= k:
                result.append(nums[queue[0]])
                left += 1
        
        return result

    def max_sliding_window_brute_force(self, nums: List[int], k: int) -> List[int]:
        """
            O(n*k), we create a k size window, and compute max as we do

            then when we reach the end of the window, we move left by one and make right = left

            to recalculate the max for that specific window

            Fails because of time limit

            https://leetcode.com/submissions/detail/849570731/
        """
        result = []

        window_max = -10 ** 4
        left = right = 0
        while left <= right and right < len(nums):
            if (right - left) != k:
                num = nums[right]
                window_max = max(num, window_max)
                right += 1
            else:
                result.append(window_max)
                window_max = -10 ** 4
                left += 1
                right = left
        else:
            result.append(window_max)
        
        return result

if __name__ == '__main__':
    obj = SlidingWindowMaximum()

    assert obj.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
    assert obj.maxSlidingWindow([1], 1) == [1]
    assert obj.maxSlidingWindow([1,3,1,2,0,5],3) == [3,3,2,5]

    