from typing import List
import heapq

class HandOfStraights:
    """
        846. Hand of Straights

        Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, 
        
        and consists of groupSize consecutive cards.

        Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, 
        
        return true if she can rearrange the cards, or false otherwise.
    """
    def is_n_straight_hand(self, hand: List[int], groupSize: int) -> bool:
        """
            O(n log(n))

            we create a minimum heap out of the cards, a minimum heap is a tree of values sorted ascending

            We basically do the same flow as the brute force solution below, 
            
            but now since we are using a heap, then we can get the

            minimum in o(1), and delete cards from it in O(log(n)) times

            https://leetcode.com/submissions/detail/853949769/
        """
        if len(hand) % groupSize != 0:
            return False

        frequency_dict = {}
        for card in hand:
            frequency_dict[card] = frequency_dict.get(card, 0) + 1

        min_heap = list(frequency_dict.keys())
        heapq.heapify(min_heap)

        while min_heap:
            minimum = min_heap[0]

            for i in range(minimum, minimum + groupSize):
                if i not in frequency_dict:
                    return False

                frequency_dict[i] -= 1
                if frequency_dict[i] == 0:
                    if i != min_heap[0]:
                        return False

                    heapq.heappop(min_heap)

        return True

    def is_n_straight_hand_brute_force(self, hand: List[int], groupSize: int) -> bool:
        """
            O(n^2)

            We create a frequency dict for all numbers, and in each iteration we find the minimum key

            And we try to find a card that is minimum + 1, if it exists and we keep creating our group until we reach 

            groupSize, if at any point that minimum + 1 card doesnt exist, then we return False

            https://leetcode.com/submissions/detail/853939420/
        """
        if len(hand) % groupSize != 0:
            return False

        frequency_dict = {}
        for card in hand:
            frequency_dict[card] = frequency_dict.get(card, 0) + 1

        current_group = []
        for _ in hand:
            if not current_group:
                current_card = min(frequency_dict.keys())
                current_group.append(current_card)
                frequency_dict[current_card] -= 1

                if frequency_dict[current_card] == 0:
                    del frequency_dict[current_card]

            else:
                next_consecutive_card = current_group[-1] + 1
                if frequency_dict.get(next_consecutive_card, 0) == 0:
                    return False
                
                frequency_dict[next_consecutive_card] -= 1
                if frequency_dict[next_consecutive_card] == 0:
                    del frequency_dict[next_consecutive_card]

                current_group.append(next_consecutive_card)

            if current_group and len(current_group) % groupSize == 0:
                current_group = []


        return True

if __name__ == '__main__':
    obj = HandOfStraights()

    assert obj.is_n_straight_hand_brute_force(hand = [1,2,3,6,2,3,4,7,8], groupSize = 3) == True