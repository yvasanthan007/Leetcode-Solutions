# Intuition
Take characters alternately from both strings and add them to the result. If one string is longer, append the remaining characters.

# Approach
1. Create an empty list to store the result.
2. Iterate up to the length of the longer string.
3. If the index exists in `word1`, add its character.
4. If the index exists in `word2`, add its character.
5. Join the list into a string and return it.

# Complexity
- Time complexity:
O(n + m)

- Space complexity:
O(n + m)

# Code
```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = []

        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                a.append(word1[i])
            if i < len(word2):
                a.append(word2[i])

        return "".join(a)
