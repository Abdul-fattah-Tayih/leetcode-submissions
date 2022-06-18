class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        first_string_chars = {}
        second_string_chars = {}

        # fill dict with characters from a to z
        for i in range(ord('a'), ord('z') + 1):
            first_string_chars[chr(i)] = 0
            second_string_chars[chr(i)] = 0
        
        # add frequencies for s1
        for character in s1:
            first_string_chars[character] += 1

        # sliding window for s2 against s1
        for idx, character in enumerate(s2):
            if idx >= len(s1):
                second_string_chars[s2[idx - len(s1)]] -= 1
            second_string_chars[character] += 1
            if first_string_chars == second_string_chars:
                return True

        return False

            

solution = Solution()
print(solution.checkInclusion("ab", "eidbaooo"))
print(solution.checkInclusion("ab", "eidboaoo"))
print(solution.checkInclusion("a", "ab"))
print(solution.checkInclusion("ab", "ab"))
print(solution.checkInclusion("hello", "ooolleoooleh"))
print(solution.checkInclusion("adc", "dcda"))
print(solution.checkInclusion("abc", "bbbca"))
