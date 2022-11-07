from typing import List

class ShuffleTheArray:
    """
        O(n)
        2 pointer solution, we put a pointer at the beggining of the array, and a pointer at n
        and we append values from each pointer in each iteration
    """
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        y_pointer = n
        shuffled_array = []

        # we don't use while because it is much slower than a normal for in python
        for x_pointer in range(n):
            shuffled_array.append(nums[x_pointer])
            shuffled_array.append(nums[y_pointer])

            y_pointer += 1

        return shuffled_array


if __name__ == '__main__':
    object = ShuffleTheArray()

    print(object.shuffle([2,5,1,3,4,7], 3))