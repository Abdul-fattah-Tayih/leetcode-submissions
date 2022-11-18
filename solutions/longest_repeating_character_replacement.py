class LongestRepeatingCharacterReplacement:
    """
        424. Longest Repeating Character Replacement

        You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. 
        
        You can perform this operation at most k times.

        Return the length of the longest substring containing the same letter you can get after performing the above operations.
    """
    def characterReplacement(self, s: str, k: int) -> int:
        """
            O(26n)

            The idea here is to expand a sliding window as long as 
            
            length of the window - the frequency of the most repeated character in the window  is less than `k`

            And the maximum size of the window resultant from this operation is longest substring with `k` replacements
        """
        character_frequency = {}
        left = right = substring_length = longest_substring_length = 0

        while left <= right and right < len(s):
            left_character = s[left]
            right_character = s[right]

            substring_length += 1
            character_frequency[right_character] = character_frequency.get(right_character, 0) + 1
            replacements_to_change_window_to_max_character = substring_length - max(character_frequency.values(), default=0)

            if replacements_to_change_window_to_max_character > k:
                character_frequency[left_character] = character_frequency.get(left_character, 1) - 1
                substring_length -= 1
                left += 1

            longest_substring_length = max(longest_substring_length, substring_length)
            right += 1

        return longest_substring_length


if __name__ == '__main__':
    obj = LongestRepeatingCharacterReplacement()
    
    assert obj.characterReplacement('ABAB', 2) == 4, f'ABAB and 2 must be equal to 4, got {obj.characterReplacement("ABAB", 2)}'
    assert obj.characterReplacement('AABABBA', 1) == 4, f'AABABBA and 1 must be equal to 4, got {obj.characterReplacement("AABABBA", 1)}'