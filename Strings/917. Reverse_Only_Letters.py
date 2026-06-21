# Intuition
Use two pointers from both ends of the string. Swap only the letters and keep non-letter characters in their original positions.

# Approach
1. Convert the string into a list.
2. Use two pointers: left and right.
3. If both characters are letters, swap them.
4. If the left character is not a letter, move left forward.
5. If the right character is not a letter, move right backward.
6. Convert the list back to a string and return it.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(n)

# Code
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        s = list(s)

        while left < right:
            if s[left].isalpha() and s[right].isalpha():
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif not s[left].isalpha():
                left += 1
            else:
                right -= 1

        return "".join(s)
