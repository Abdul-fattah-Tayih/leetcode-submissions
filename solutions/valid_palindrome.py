from re import findall

"""
Question 125
Valid Palindrome
O(n)
"""
class ValidPalindrome:
    def isPalindrome(self, s: str) -> bool:
        # normalize the string as per requirements, remove all non-alphanumeric characters
        s = ''.join(findall('[a-zA-Z0-9]', s))

        left = 0
        right = len(s) - 1

        # the technique here is to use 2 pointers, on on each end of the string and compare the characeters
        # then we move the 2 pointers in their corresponding direction
        while left < right:
            left_char = s[left].lower()
            right_char = s[right].lower()

            if left_char != right_char:
                return False
            
            left += 1
            right -= 1

        return True

if __name__ == '__main__':
    object = ValidPalindrome()

    print(object.isPalindrome("A man, a plan, a canal: Panama"))
    print(object.isPalindrome("race a car"))
    print(object.isPalindrome(" "))