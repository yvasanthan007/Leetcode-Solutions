# Intuition
For each character in the string, find the shortest distance to the target character by checking all occurrences of the target.

# Approach
1. Traverse each position in the string.
2. For every position, check all positions containing the target character.
3. Calculate the distance between the current position and each target position.
4. Store the minimum distance.
5. Return the list of distances.

# Complexity
- Time complexity:
O(n²)

- Space complexity:
O(n)

# Code
```python
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        a = []

        for i in range(n):
            min_dis = float('inf')

            for j in range(n):
                if s[j] == c:
                    min_dis = min(min_dis, abs(i - j))

            a.append(min_dis)

        return a
