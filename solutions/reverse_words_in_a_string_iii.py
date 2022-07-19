class ReverseWordsInAStringThree:
    def reverseWords(self, s: str) -> str:
        current_word = ""
        reversed_string = ""
        for idx, char in enumerate(s):
            if char == ' ' or idx == len(s) - 1:
                current_word = char + current_word if idx == len(s) - 1 else current_word + char
                reversed_string += current_word
                current_word = ''
            else:
                current_word = char + current_word

        return reversed_string

    def reverseWordsSplit(self, s: str) -> str:
        words = s.split(' ')
        result = []

        for word in words:
            result.append(word[::-1])
            result.append(' ')

        ''.join(result)

if __name__ == '__main__':
    solution = ReverseWordsInAStringThree()
    result = solution.reverseWords("Let's take LeetCode contest")
    print(result)

    result = solution.reverseWords("God Ding")
    print(result)