from typing import Counter


class PermutationInString5Oct2024:
    """
        567. Permutation in String

        Given two strings s1 and s2, return true if s2 contains a 
        permutation
        of s1, or false otherwise.

        In other words, return true if one of s1's permutations is the substring of s2.

        

        Example 1:

        Input: s1 = "ab", s2 = "eidbaooo"
        Output: true
        Explanation: s2 contains one permutation of s1 ("ba").
        Example 2:

        Input: s1 = "ab", s2 = "eidboaoo"
        Output: false
        

        Constraints:

        1 <= s1.length, s2.length <= 104
        s1 and s2 consist of lowercase English letters.
    """
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
            Frequency hashmap (counter) and sliding window solution

            We create a hashmap containing all characters and their frequencies for s1

            Then we create a window the same size as s1, and store a hashmap with the occurences of each character in that window

            when the size of the window matches s1, we compare the hashmaps, and if they match we return true otherwise we keep going
        """
        s1_dict = Counter(s1)
        window_dict = Counter()
        left = 0
        
        for right in range(len(s2)):
            while right - left + 1 > len(s1):
                if window_dict == s1_dict:
                    return True

                window_dict[s2[left]] -= 1
                if window_dict[s2[left]] <= 0:
                    del window_dict[s2[left]]

                left += 1

            if right - left + 1 == len(s1) and window_dict == s1_dict:
                    return True

            window_dict[s2[right]] = window_dict.get(s2[right], 0) + 1

        return window_dict == s1_dict
    
if __name__ == '__main__':
    solution = PermutationInString5Oct2024()
    print(solution.checkInclusion("ab", "eidbaooo"))
    print(solution.checkInclusion("ab", "eidboaoo"))
    print(solution.checkInclusion("a", "ab"))
    print(solution.checkInclusion("ab", "ab"))
    print(solution.checkInclusion("hello", "ooolleoooleh"))
    print(solution.checkInclusion("adc", "dcda"))
    print(solution.checkInclusion("abc", "bbbca"))