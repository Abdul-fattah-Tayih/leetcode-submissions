from typing import List


class MinimumNumberOfArrowsToBurstBalloons:
    """
        452. Minimum Number of Arrows to Burst Balloons

        There are some spherical balloons taped onto a flat wall that represents the XY-plane. 

        The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] 

        denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

        Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. 

        A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot.

        A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

        Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
    """

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
            O(n log(n))
        """
        if not points:
            return 0

        points.sort(key=lambda point: point[0])  # sort points by start
        
        previous_balloon = points[0]
        total = 1

        for start, end in points[1:]:
            if start <= previous_balloon[1]:
                previous_balloon[1] = min(end, previous_balloon[1])
            else:
                total += 1
                previous_balloon = [start, end]

        return total

if __name__ == '__main__':
    obj = MinimumNumberOfArrowsToBurstBalloons()

    assert obj.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]) == 2
    assert obj.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]) == 4
    assert obj.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]) == 2