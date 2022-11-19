class MinimumWindowSubstring:
    """
        76. Minimum Window Substring

        Given two strings s and t of lengths m and n respectively, return the minimum window substring of s 
        
        such that every character in t (including duplicates) is included in the window. 
        
        If there is no such substring, return the empty string "".

        The testcases will be generated such that the answer is unique.
    """
    def minWindow(self, s: str, t: str) -> str:
        """
            O(n^2), sliding window, keep going right until we find a matching window

            then we move left until the window is not matching, and repeat

            once we reach the end of the array we would find the shortest window
        """
        left = 0
        window_length = 0
        min_window_length = max(len(s), len(t))
        min_window_coordinates = (0, 0)
        found_min = False

        t_chars = {}
        for char in t:
            t_chars[char] = t_chars.get(char, 0) + 1

        found_chars = {}
        for right in range(len(s)):
            character = s[right]

            if character in t_chars:
                found_chars[character] = found_chars.get(character, 0) + 1

            window_length += 1
            
            while self.dicts_are_matched(t_chars, found_chars):
                if window_length <= min_window_length:
                    min_window_coordinates = (left, right)
                    min_window_length = window_length
                    found_min = True
                
                if s[left] in found_chars:
                    found_chars[s[left]] -= 1

                left += 1
                window_length -= 1

        return s[min_window_coordinates[0]:min_window_coordinates[1] + 1] if found_min else ""
    
    def dicts_are_matched(self, dict_to_compare_from: 'dict[str, str]', dict_to_compare_to: 'dict[str, str]') -> bool:
        if len(dict_to_compare_from) != len(dict_to_compare_to):
            return False

        for key, value in dict_to_compare_from.items():
            compare_to_value = dict_to_compare_to[key]

            if value > compare_to_value:
                return False

        return True

if __name__ == '__main__':
    obj = MinimumWindowSubstring()

    assert obj.minWindow("ADOBECODEBANC", "ABC") == 'BANC'
    assert obj.minWindow("a", "a") == 'a'