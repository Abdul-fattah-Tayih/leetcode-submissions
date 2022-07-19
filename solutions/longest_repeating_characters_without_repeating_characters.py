class LongestRepeatingCharactersWithoutRepeatingCharacters:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: return len(s)
        max_substring_length, current_substring_length = 0, 1
        found_chars = set([s[0]])
        left, right = 0, 1
        
        while left <= right and right < len(s):
            left_char = s[left]
            right_char = s[right]
            
            if right_char in found_chars:
                current_substring_length -= 1
                found_chars.remove(left_char)
                left += 1
            else:
                current_substring_length += 1
                max_substring_length = max(max_substring_length, current_substring_length)
                found_chars.add(right_char)
                right += 1

        return max_substring_length

if __name__ == '__main__':
    solution = LongestRepeatingCharactersWithoutRepeatingCharacters()
    print(solution.lengthOfLongestSubstring("abcabcbb"))
    print(solution.lengthOfLongestSubstring("bbbbb"))
    print(solution.lengthOfLongestSubstring("pwwkew"))