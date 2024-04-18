class LengthOfLastWord:
    """
        58. Length of Last Word
    
        Given a string s consisting of words and spaces, return the length of the last word in the string.

        A word is a maximal substring consisting of non-space characters only.
    """
    def lengthOfLastWord(self, s: str) -> int:
        result = 0
        current_word_length = 0

        for char in s:
            if char == ' ':
                if current_word_length > 0:
                    result = current_word_length

                current_word_length = 0
            else:
                current_word_length += 1

        if current_word_length != 0:
            return current_word_length

        return result
    
if __name__ == "__main__":
    obj = LengthOfLastWord()
    print(obj.lengthOfLastWord("luffy is still joyboy"))