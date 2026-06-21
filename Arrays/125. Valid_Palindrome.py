# Intuition
Remove all non-alphanumeric characters and compare the string with its reverse.

# Approach
1. Traverse the string and keep only alphanumeric characters.
2. Convert all characters to lowercase.
3. Build a cleaned string.
4. Compare the cleaned string with its reverse.
5. If both are equal, it is a palindrome.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(n)

# Code
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ""

        for ch in s:
            if ch.isalnum():
                a += ch.lower()

        return a == a[::-1]
