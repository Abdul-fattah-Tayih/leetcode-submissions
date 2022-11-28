class ValidAnagram:
    """
        242. Valid Anagram

        Given two strings s and t, return true if t is an anagram of s, and false otherwise.

        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
        
        typically using all the original letters exactly once.
    """
    def isAnagram(self, s: str, t: str) -> bool:
        """
            O(n)

            We create a frequency dict for both strings, if both dicts are equal

            then the 2 strings are anagrams, otherwise they're not

            We can even do the equality check of the dicts manually, 
            
            first we check if they have equal amount of keys and if not then they're not the same, 
            
            Then we need to iterate over one dict and check if all the values of each character are the same

            https://leetcode.com/submissions/detail/851190369/
        """
        s_dict = {}
        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1
            
        t_dict = {}
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1
            
        return s_dict == t_dict

if __name__ == '__main__':
    obj = ValidAnagram()

    assert obj.isAnagram(s = "anagram", t = "nagaram") == True
    assert obj.isAnagram(s = "rat", t = "car") == False