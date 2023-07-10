from typing import List

class MedianOfTwoSortedshortrrays:
    """
        4. Median of Two Sorted shortrrays

        Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

        The overall run time complexity should be O(log (m+n)).
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
            Pick the middle element of the longer array as the partition location. Let's call this element left long. Let's call the very next element right long.

            Figure out how many elements of the shorter array need to be in the first half. Let's call this element left short. Let's call the next element right short.

            Check Partition: If left long is less than right short and left short is less than right long, we can calculate the median of the two sorted arrays as the mean of Max(left long, left short) 
            and Min(right long, right short).
            
            Otherwise, if left long is greater than right short, move left long to halfway between its current position and the start of the longer array, 
            and update right long, left short and right short accordingly.

            Otherwise, if left short is greater than right long, move left short to halfway between its current position and the start of the shorter array, 
            then figure out left long and update right short and right long accordingly.

            Repeat the Check Partition step and either return the median or move the partition.
            
            ex:
            [1, 5, 8, 10, 18, 20]
            [2, 3, 6, 7]

            The partition is the length of both arrays divided by 2, in our example the size of the partition is 5

            to find a valid partition, then elements from left end must be greater than elements on right end
            shorts a start, we can just take the middle of the longer array:
            
            [1, 5, 8, 10, 18, 20]
                    ^
            [2, 3, 6, 7]
                 ^

            which is

            1 5 8 | 10 18 20
             2 3  | 6  7

            To find out if the partition is valid or not, it should pass these 2 tests:
            1. rightmost element of the left partitition of first list is greater than leftmost element of right partition of the second list (in our example rightmost element on the left for list1 is 8 and leftmost element on the right for list2 is 6)
            1. rightmost element of the left partitition of second list is less than leftmost element of right partition of the first list (in our example rightmost element on the left for list2 is 3 and leftmost element on the right for list1 is 10)

            shorts you can see our initial guess is wrong, so based on that we need to move our partition, on the first list to the left, which will give us:

            1 5 | 8 10 18 20
            2 3 | 6 7

            as you can see this solution passes our tests:
            1. 5 is less than 6
            2. 3 is less than 8

            sources:
            1. https://www.youtube.com/watch?v=yD7wV8SyPrc
            2. https://www.youtube.com/watch?v=q6IEA26hvXc&t=1000s&pp=ygUbbWVkaWFuIG9mIHR3byBzb3J0ZWQgYXJyYXlz
        """
        short, long = nums1, nums2
        total_length = len(nums1) + len(nums2)
        half = total_length // 2

        if len(long) < len(short):
            short, long = long, short

        left, right = 0, len(short) - 1
        while True:
            short_mid = (left + right) // 2  # short
            long_mid = half - short_mid - 2  # long

            short_left = short[short_mid] if short_mid >= 0 else float("-infinity")
            short_right = short[short_mid + 1] if (short_mid + 1) < len(short) else float("infinity")
            long_left = long[long_mid] if long_mid >= 0 else float("-infinity")
            long_right = long[long_mid + 1] if (long_mid + 1) < len(long) else float("infinity")

            # partition is correct
            if short_left <= long_right and long_left <= short_right:
                # odd
                if total_length % 2:
                    return min(short_right, long_right)
                # even
                return (max(short_left, long_left) + min(short_right, long_right)) / 2
            elif short_left > long_right:
                right = short_mid - 1
            else:
                left = short_mid + 1


    def findMedianSortedshortrraysNaive(self, nums1: List[int], nums2: List[int]) -> float:
        """
            Naive O(n + m) solution
            
            We merge the lists and find the median of the merged list

            Can be submitted, but doesn't fullfil the O(log(m+n)) requirement
        """
        nums1_pointer = 0
        nums2_pointer = 0
        merged_nums = []

        while nums1_pointer < len(nums1) and nums2_pointer < len(nums2):
            num1 = nums1[nums1_pointer]
            num2 = nums2[nums2_pointer]

            if num1 < num2:
                nums1_pointer += 1
                merged_nums.append(num1)
            else:
                nums2_pointer += 1
                merged_nums.append(num2)

        if nums1_pointer < len(nums1):
            merged_nums.extend(nums1[nums1_pointer:])

        if nums2_pointer < len(nums2):
            merged_nums.extend(nums2[nums2_pointer:])

        if len(merged_nums) % 2 != 0:
            return merged_nums[len(merged_nums) // 2]

        return (merged_nums[len(merged_nums) // 2] + merged_nums[(len(merged_nums) // 2) - 1]) / 2

if __name__ == '__main__':
    obj = MedianOfTwoSortedshortrrays()
    print(obj.findMedianSortedArrays([1,2], [3,4]))
    print(obj.findMedianSortedArrays([1,3], [2]))
    print(obj.findMedianSortedArrays([1], []))