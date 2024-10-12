from heapq import heappop, heappush
from typing import List


class TheNumberOftheSmallestUnoccupiedChair:
    """
        1942. The Number of the Smallest Unoccupied Chair

        There is a party where n friends numbered from 0 to n - 1 are attending. There is an infinite number of chairs in this party that are numbered from 0 to infinity. When a friend arrives at the party, they sit on the unoccupied chair with the smallest number.

        For example, if chairs 0, 1, and 5 are occupied when a friend comes, they will sit on chair number 2.
        When a friend leaves the party, their chair becomes unoccupied at the moment they leave. If another friend arrives at that same moment, they can sit in that chair.

        You are given a 0-indexed 2D integer array times where times[i] = [arrivali, leavingi], indicating the arrival and leaving times of the ith friend respectively, and an integer targetFriend. All arrival times are distinct.

        Return the chair number that the friend numbered targetFriend will sit on.
    """
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        """
            2 Heaps solution

            We use 2 heaps (i initially tried only using 1, ill explain why that won't work)
            
            One heap to keep track of the available seats, we will use the min heap so we can always have the smallest available chair

            The other heap is to track the unavailable seats, we will use the min heap so we can remove the seats with the minimum leaving time

            The Algorithm:
                - Sort the input based on arrival time
                - Initialize the 2 heaps
                - in each iteration, we check the arrival time of the friend
                    - if the friend arrives after previous friends leave, we empty their chairs
                    - add the friend to the smallest available chair
            
            Why we need to keep track of available seats is to handle cases where friends come early and others come after them and stay for a long time,
            this will cause an empty section in the middle, and without tracking this we assume that friends always sit at the end, this works for 49/65 cases surprisingly
        """
        if not times:
            return 0

        times = sorted([
            (arrival, leave, index) for index, (arrival, leave) in enumerate(times)
        ])

        next_seat = 0
        available_seats = []
        occupied_seats = []

        for time in times:
            arrival, leaving, index = time

            while occupied_seats and occupied_seats[0][0] <= arrival:
                _, chair = heappop(occupied_seats)
                heappush(available_seats, chair)

            if available_seats:
                current_seat = heappop(available_seats)
            else:
                current_seat = next_seat
                next_seat += 1

            heappush(occupied_seats, (leaving, current_seat))
            
            if index == targetFriend:
                return current_seat

        return 0
    
if __name__ == "__main__":
    obj = TheNumberOftheSmallestUnoccupiedChair()
    print(obj.smallestChair(times = [[1,4],[2,3],[4,6]], targetFriend = 1))
    print(obj.smallestChair(times = [[3,10],[1,5],[2,6]], targetFriend = 0))
    print(obj.smallestChair([[33889,98676],[80071,89737],[44118,52565],[52992,84310],[78492,88209],[21695,67063],[84622,95452],[98048,98856],[98411,99433],[55333,56548],[65375,88566],[55011,62821],[48548,48656],[87396,94825],[55273,81868],[75629,91467]], 6))