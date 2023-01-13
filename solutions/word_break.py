from typing import List, Set

class WordBreak:
    """
        139. Word Break

        Given a string s and a dictionary of strings wordDict, 
        
        return true if s can be segmented into a space-separated sequence of one or more dictionary words.

        Note that the same word in the dictionary may be reused multiple times in the segmentation.
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # TODO
        return self.word_break_recursive(s, set(wordDict), '', s)

    def word_break_recursive(self, s: str, words: Set, current_word: str, remaining_word: str, i: int = 0) -> bool:
        if i == len(s):
            if current_word in words:
                remaining_word = s[i:]

            return len(remaining_word) == 0

        # if remaining word is empty return true
        if not remaining_word:
            return True

        # chop word if current word is in the set
        if current_word in words:
            self.word_break_recursive(s, words, '', s[i:], i)

        # include current character
        inclusive = self.word_break_recursive(s, words, current_word + s[i], remaining_word, i + 1)       

        return inclusive
        
    def word_break_iterative_without_backtracking(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)

        string_remainder = s
        current_word = ''
        for index, char in enumerate(s):
            current_word += char

            if current_word in words:
                string_remainder = s[index + 1:]
                current_word = ''

            if string_remainder in words:
                return True
        
        return len(string_remainder) == 0

if __name__ == '__main__':
    obj = WordBreak()

    # assert obj.wordBreak('leetcode', ['leet', 'code']) == True
    # assert obj.wordBreak("applepenapple", ["apple","pen"]) == True
    assert obj.wordBreak("catsandog", ["cats","dog","sand","and","cat"]) == False
    assert obj.wordBreak("bb", ["a","b","bbb","bbbb"]) == True
    assert obj.wordBreak("aaaaaaa", ["aaaa","aaa"]) == True
    assert obj.wordBreak("goalspecial", ["go","goal","goals","special"]) == True