# Intuition
'''Reverse the given number and compare it with the original number. If both are the same, it is a palindrome.'''

# Approach
''' 1. Store the original number.
    2. Reverse the number digit by digit.
    3. Compare the reversed number with the original number.
    4. Return `True` if they are equal, otherwise return `False`.'''

# Complexity
''' - Time complexity:
        O(log n)

    - Space complexity:
        O(1)'''

# Code
class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = x
        rev = 0

        while x > 0:
            b = x % 10
            rev = rev * 10 + b
            x //= 10

        return rev == a
