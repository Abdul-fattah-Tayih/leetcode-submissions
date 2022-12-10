from typing import List

class NonOverlappingIntervals:
    """
        435. Non-overlapping Intervals

        Given an array of intervals intervals where intervals[i] = [starti, endi]
        
        return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
    """

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
            O(n log(n))

            
        """
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res