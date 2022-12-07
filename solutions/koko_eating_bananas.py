from typing import List
from math import ceil

class KokoEatingBananas:
    """
        875. Koko Eating Bananas

        Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
        
        The guards have gone and will come back in h hours.

        Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats 
        
        k bananas from that pile. If the pile has less than k bananas, 
        
        she eats all of them instead and will not eat any more bananas during this hour.

        Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

        Return the minimum integer k such that she can eat all the bananas within h hours.
    """
    def min_eating_speed(self, piles: List[int], h: int) -> int:
        """
            O(log(max(piles)) * n)

            The biggest improvement we can do here is to binary search over the range of eating speeds, which is 1, ..., max(piles)

            We don't need to create an array of ranges to binary search, we just put left at 1 and right at max(piles)

            And then we manipulate them in accordance with binary search, and instead of indices, the values are the actual eating speed

            https://leetcode.com/problems/koko-eating-bananas/submissions/855850639/
        """
        left = 1
        right = max(piles)
        min_eating_speed = right
        while left <= right:
            eating_speed = left + (right - left) // 2
            hours_elapsed = 0
            for pile in piles:
                if pile <= eating_speed:
                    hours_elapsed += 1
                else:
                    hours_elapsed += ceil(pile / eating_speed)
            
            if hours_elapsed > h:
                left = eating_speed + 1
            else:
                right = eating_speed - 1
                min_eating_speed = min(min_eating_speed, eating_speed)

        return left


    def min_eating_speed_brute_force(self, piles: List[int], h: int) -> int:
        """
            O(max(piles) * n)

            Brute force solution, we iterate from 1 to max(piles)

            and in each iteration we calculate the number of hours needed to eat the pile as defined in our minimum

            which is the pile / min_eating_speed, and we keep adding the hours and we return the first number that finishes

            all the piles in the given hours

            Fails due to time constraints

            https://leetcode.com/problems/koko-eating-bananas/submissions/855844780/
        """
        min_eating_speed = 1
        max_eating_speed = max(piles)
        while min_eating_speed <= max_eating_speed:
            hours_elapsed = 0
            for pile in piles:
                if pile <= min_eating_speed:
                    hours_elapsed += 1
                else:
                    hours_elapsed += ceil(pile / min_eating_speed)
            
            if hours_elapsed <= h:
                break

            min_eating_speed += 1

        return min_eating_speed

if __name__ == '__main__':
    obj = KokoEatingBananas()

    assert obj.min_eating_speed([3,6,7,11], 8) == 4
    assert obj.min_eating_speed([30,11,23,4,20], 5) == 30
    assert obj.min_eating_speed([30,11,23,4,20], 6) == 23
    assert obj.min_eating_speed([312884470], 312884469) == 2