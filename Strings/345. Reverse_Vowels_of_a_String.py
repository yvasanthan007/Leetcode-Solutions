# Intuition
Use two pointers from both ends of the string and swap only the vowels while keeping other characters in their original positions.

# Approach
1. Convert the string into a list.
2. Use two pointers: left and right.
3. If both characters are vowels, swap them.
4. If the left character is not a vowel, move left forward.
5. If the right character is not a vowel, move right backward.
6. Continue until the pointers meet.
7. Convert the list back to a string and return it.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(n)

# Code
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] in 'AEIOUaeiou' and s[right] in 'AEIOUaeiou':
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left] not in 'AEIOUaeiou':
                left += 1
            elif s[right] not in 'AEIOUaeiou':
                right -= 1

        return "".join(s)
