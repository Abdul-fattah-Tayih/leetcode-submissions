from typing import List

class VerifyingAnAlienDictionary:
    """
        953. Verifying an Alien Dictionary

        In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order.
        
        The order of the alphabet is some permutation of lowercase letters.

        Given a sequence of words written in the alien language, and the order of the alphabet, 
        
        return true if and only if the given words are sorted lexicographically in this alien language.
    """
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """
            O(n * m), n being the number of words, and m being the character count of the longest word

            We create a dict, keys are the characters, and the value being the index of that character which is also the order

            of that character, then we loop over words, in each iteration, we check the current word and the next word

            and then we loop over the characters of the first word, and we want to search for the first differing character

            between them, then we use our order dictionary to find the order of both characters, if the first word has

            lower order than the 2nd word then the 2 words are sorted correctly and we can check then next words

            otherwise we return False

            https://leetcode.com/submissions/detail/853956454/
        """
        order_dict = {char: index for index, char in enumerate(order)}

        for index, word in enumerate(words):
            if index + 1 == len(words):
                break

            word2 = words[index + 1]

            for character_index, character in enumerate(word):
                if character_index == len(word2):
                    return False

                character2 = word2[character_index]
                if character != character2:
                    if order_dict[character] > order_dict[character2]:
                        return False
                    
                    break

        return True

if __name__ == '__main__':
    obj = VerifyingAnAlienDictionary()

    assert obj.isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz") == True