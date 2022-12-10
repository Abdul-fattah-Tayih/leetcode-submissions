from typing import List
from collections import deque

class LetterCombinationsOfAPhoneNumber:
    """
        17. Letter Combinations of a Phone Number

        Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
        
        Return the answer in any order.

        A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
    """

    LETTER_VALUES = {
        '2': ["a", "b", "c"],
        '3': ["d", "e", "f"],
        '4': ["g", "h", "i"],
        '5': ["j", "k", "l"],
        '6': ["m", "n", "o"],
        '7': ["p", 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def letter_combinations_brute_force(self, digits: str) -> List[str]:
        """
            O(n*v) BFS

            I have absolutely no idea how this is accepted!

            What I did here is I create a deque (this is because I want delete operations at the left to be O(1))

            And add a list of the characters that correspond to first digit to it
            
            Then I iterate over the characters of the next digit and pop each old digit from the deque

            and concatenate them together, and keep going until we've covered all the digits

            This is probably not an idea answer but it's what I came up with, so I'll keep it here for reference only

            https://leetcode.com/submissions/detail/853909960/
        """
        result = deque()

        for digit in digits:
            if result:
                current_character_length = len(result)
                for _ in range(current_character_length):
                    item = result.popleft()
                    for char in self.LETTER_VALUES.get(digit, []):
                        result.append(item + char)
            else:
                for char in self.LETTER_VALUES.get(digit, []):
                    result.append(char)

        return list(result)

if __name__ == '__main__':
    obj = LetterCombinationsOfAPhoneNumber()

    assert obj.letter_combinations_brute_force('23') == ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    assert obj.letter_combinations_brute_force('') == []
    assert obj.letter_combinations_brute_force('2') == ['a', 'b', 'c']
