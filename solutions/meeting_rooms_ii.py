from typing import List
from heapq import heappush, heappop

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.closed = True  # by default, the interval is closed

    # set the flag for closed/open
    def set_closed(self, closed):
        self.closed = closed

    def __str__(self):
        return "[" + str(self.start) + ", " + str(self.end) \
              + "]" if self.closed else "(" + str(self.start) + ", " \
              + str(self.end) + ")"


def find_sets(intervals: List[Interval]):
    """
        253. Meeting Rooms II

        Given a list of meeting time intervals as input, find the minimum number of meeting rooms needed to hold these meetings.
        
        O(n)
    """
    if not intervals:
        return 0

    heap = []
    intervals.sort(key=lambda x: x.start)
    heappush(heap, intervals[0].end)

    for interval in intervals[1:]:
        if heap[0] <= interval.start:
            heappop(heap)

        heappush(heap, interval.end)

    return len(heap)