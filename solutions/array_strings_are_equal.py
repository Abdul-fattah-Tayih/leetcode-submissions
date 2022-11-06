from typing import List

class ArrayStringsAreEqual:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        first_word_concatenated = ''.join(word1)
        
        return first_word_concatenated == ''.join(word2)