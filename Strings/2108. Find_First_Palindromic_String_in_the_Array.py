# Intuition
Check each word in the array and return the first word that reads the same forward and backward.

# Approach
1. Traverse the array of words.
2. Reverse each word.
3. Compare the word with its reverse.
4. If they are equal, return the word.
5. If no palindrome is found, return an empty string.

# Complexity
- Time complexity:
O(n × m)

- Space complexity:
O(m)

# Code
```python
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            a = i
            b = i[::-1]

            if a == b:
                return a

        return ""
