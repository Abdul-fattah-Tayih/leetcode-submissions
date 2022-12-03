from typing import List

class GroupAnagrams:
    """
        49. Group Anagrams

        Given an array of strings strs, group the anagrams together. You can return the answer in any order.

        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
        
        typically using all the original letters exactly once.
    """
    def group_anagrams_sort(self, strs: List[str]) -> List[List[str]]:
        """
            O(n * m log(m))

            We sort the letters of each string, which creates a unique string for all anagrams

            Then we store an array in the dict for each sorted string, and add strings that match to that array

            In the end, we just return the values of the dict (because we don't need the keys)

            eg:

            'eat', 'tea', 'ate' are all equal to aet when sorted,

            so in our dict we will have:
            
            {
                "aet": ['eat', 'tea', 'ate']
            }

            https://leetcode.com/submissions/detail/852227079/
        """
        result = {}

        for string in strs:
            sorted_string = "".join(sorted(string))

            if sorted_string in result:
                result[sorted_string].append(string)
            else:
                result[sorted_string] = [string]

        return result.values()

    def group_anagrams_brute_force(self, strs: List[str]) -> List[List[str]]:
        """
            O(n * m^2) n: length of array, m: length of longest word(s)

            we create a frequency dict for all the words in the array

            then we compare every word with the rest of the array using the dicts we created

            Whenever we add a word to the result, we skip that index so we dont get duplicate groups

            Fails due to time constraints

            https://leetcode.com/submissions/detail/852220825/
        """
        result = []
        string_frequency = []

        for string in strs:
            frequency = {}
            for char in string:
                frequency[char] = frequency.get(char, 0) + 1

            string_frequency.append(frequency)

        checked_word_indices = set()
        for index, string in enumerate(strs):
            group = []
            frequency = string_frequency[index]

            for frequency_index, frequency_dict in enumerate(string_frequency):
                if frequency_index in checked_word_indices:
                    continue

                if frequency_dict == frequency:
                    group.append(strs[frequency_index])
                    checked_word_indices.add(frequency_index)

            if group:
                result.append(group)

        return result

if __name__ == '__main__':
    obj = GroupAnagrams()

    assert obj.group_anagrams_sort(["eat","tea","tan","ate","nat","bat"]) == [["bat"],["nat","tan"],["ate","eat","tea"]]
    assert obj.group_anagrams_sort([""]) == [[""]]
    assert obj.group_anagrams_sort(["a"]) == [["a"]]
