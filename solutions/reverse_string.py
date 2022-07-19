class ReverseString(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1

        return s
        
if __name__ == '__main__':
    solution = ReverseString()
    print(solution.reverseString(["h","e","l","l","o"]))
    print(solution.reverseString(["H","a","n","n","a","h"]))