from typing import List

class MaxSubsequence:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        subsequences = []
        def find_subsequences(i, current_subsequence: List, length):
            if length == k:
                subsequences.append(current_subsequence.copy())
                return current_subsequence

            for j in range(i + 1, len(nums1)):
                current_subsequence.append((nums1[j], j))
                find_subsequences(j, current_subsequence, length + 1)
                current_subsequence.pop()
                find_subsequences(j, current_subsequence, length)

            return current_subsequence

        find_subsequences(-1, [], 0)
        
        max_score = 0
        for subsequence in subsequences:
            current_score = 0
            nums2_min = 10 ** 5
            for number, index in subsequence:
                nums2_min = min(nums2_min, nums2[index])
                current_score += number

            max_score = max(max_score, (current_score * nums2_min))

        return max_score

if __name__ == '__main__':
    obj = MaxSubsequence()
    obj.maxScore(nums1 = [1,3,3,2], nums2 = [2,1,3,4], k =3)