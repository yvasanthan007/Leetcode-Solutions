# Intuition
Extract all words from the string and rebuild the string by adding the words in reverse order.

# Approach
1. Traverse the string and collect each word.
2. Ignore extra spaces.
3. Store all words in a list.
4. Traverse the list in reverse order.
5. Join the words with a single space.
6. Return the resulting string.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(n)

# Code
```python
class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = ""

        for ch in s:
            if ch != ' ':
                word += ch
            else:
                if word:
                    words.append(word)
                    word = ""

        if word:
            words.append(word)

        res = ""

        for i in range(len(words) - 1, -1, -1):
            res += words[i]
            if i > 0:
                res += ' '

        return res
