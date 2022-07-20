from typing import List

class RemoveElement:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
            Time complexity: O(n)
            Space complexity: O(1)
            Explanation: we need to move the numbers that are equal to val to the back of the list, and by extension move
                all non matching numbers to the front, and after the new length of the list, we dont care what the items are, so
                we mark a pointer at the begining, and whenever we find a non matching item we swap it with that pointer
                and increment the pointer
        """
        # Counter for keeping track of elements other than val
        count = 0

        # Loop through all the elements of the array
        for number in nums:
            # as long as the number doesnt equal the value, we move it to the beginning of the array
            if number != val:
                nums[count] = number
                count += 1

        return count
    
if __name__ == '__main__':
    solution = RemoveElement()
    print(solution.removeElement([3,2,2,3], 3))
    print(solution.removeElement([0,1,2,2,3,0,4,2], 2))
