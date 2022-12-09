from typing import List


class MergeIntervals:
    """
        56. Merge Intervals

        Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
        
        and return an array of the non-overlapping intervals that cover all the intervals in the input.
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
            O(n log(n))

            We sort the intervals, and then iterate over the them using two pointers

            If we find an overlapping interval we keep going left
            
            otherwise, we check if there's an existing overlapping interval, if so we store it and move left

            If there's no overlapping interval we just go right

            https://leetcode.com/problems/merge-intervals/submissions/856949286/
        """
        intervals = sorted(intervals)
        left = right = 0

        result = []
        overlapping_interval = None
        while left <= right and right < len(intervals):
            if self.intervals_are_overlapping(overlapping_interval or intervals[left], intervals[right]):
                overlapping_interval = [
                    intervals[left][0],
                    max(intervals[left][1], intervals[right][1],
                        overlapping_interval[1] if overlapping_interval else -10**4)
                ]
                right += 1
            else:
                if overlapping_interval:
                    result.append(overlapping_interval)
                    overlapping_interval = None
                    left = right
                else:
                    right += 1

        if overlapping_interval:
            result.append(overlapping_interval)

        return result

    def intervals_are_overlapping(self, interval1: List[int], interval2: List[int]) -> bool:
        if interval1[1] > interval2[1]:
            return interval2[1] >= interval1[0] and interval2[1] <= interval1[1]
        elif interval1[1] < interval2[1]:
            return interval1[1] >= interval2[0] and interval1[1] <= interval2[1]
        else:
            return True


if __name__ == '__main__':
    obj = MergeIntervals()

    assert obj.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert obj.merge([[1, 4], [0, 4]]) == [[0, 4]]
    assert obj.merge([[1, 4], [0, 1]]) == [[0, 4]]
    assert obj.merge([[1, 4], [0, 2], [3, 5]]) == [[0, 5]]
    assert obj.merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]) == [[1, 10]]
    assert obj.merge([[1, 3]]) == [[1, 3]]
    assert obj.merge([[2, 3], [2, 2], [3, 3], [1, 3], [5, 7],[2, 2], [4, 6]]) == [[1, 3], [4, 7]]
    assert obj.merge([[1, 3], [0, 2], [2, 3], [4, 6], [4, 5], [5, 5], [0, 2], [3, 3]]) == [[0, 3], [4, 6]]
