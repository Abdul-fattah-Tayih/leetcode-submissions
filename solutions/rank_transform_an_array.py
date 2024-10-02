from typing import List


class ArrayRankTransform:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = list(sorted(arr))
        ranks = [0] * len(arr)
        num_rank_dict = {}

        last_rank = 0
        for i, num in enumerate(sorted_arr):
            rank = i + 1
            if last_rank:
                if sorted_arr[i] == sorted_arr[i - 1]:
                    rank = last_rank
                else:
                    rank = last_rank + 1

            last_rank = rank

            num_rank_dict[num] = rank

        for i, num in enumerate(arr):
            ranks[i] = num_rank_dict[num]

        return ranks

if __name__ == "__main__":
    obj = ArrayRankTransform()

    print(obj.arrayRankTransform([100, 100,100]))