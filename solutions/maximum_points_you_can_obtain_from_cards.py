from typing import List
import unittest

class MaximumPointsYouCanObtainFromCards:
    def max_score(self, card_points: List[int], k: int) -> int:
        """
            Fixed sliding window, but instead of calculating inside the window, we calculate on either side of the window
            Time complexity: O(k)
            Space Complexity: O(1)
        """
        left = 0
        right = len(card_points) - k
        
        current_sum = sum(card_points[right:])
        max_sum = current_sum

        while right < len(card_points):
            current_sum += (card_points[left] - card_points[right])
            max_sum = max(max_sum, current_sum)
            left += 1
            right += 1
        
        return max_sum

    def max_score_naive(self, card_points: List[int], k: int) -> int:
        """
            Brute force solution, calculates every possible sum, but fails on leetcode because of timeout in large inputs
            Time complexity: O(k^2)
            Space complexity: O(1)
        """
        max_sum = 0
        current_sum = 0
        cards_last_index = len(card_points) - 1
        for idx in range(cards_last_index, cards_last_index - k, -1):
            current_sum += card_points[idx]
            max_sum = max(max_sum, current_sum)

        current_sum = 0
        for idx in range(k):
            current_sum += card_points[idx]
            max_sum = max(max_sum, current_sum)    
        
        for idx in range(k):
            current_sum = sum(card_points[:idx]) if idx > 0 else 0
            current_sum += card_points[idx]
            for right in range(cards_last_index, cards_last_index - k + idx + 1, -1):
                current_sum += card_points[right]
            
            max_sum = max(max_sum, current_sum)
        
        return max_sum

if __name__ == '__main__':
    test_runner = unittest.main('tests.test_maximum_points_you_can_obtain_from_cards', exit=False)