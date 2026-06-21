# Intuition
Convert each number to a string and check if the number of digits is even.

# Approach
1. Initialize a counter.
2. Traverse the array.
3. Convert each number to a string.
4. Check if the length of the string is even.
5. If yes, increment the counter.
6. Return the counter.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(1)

# Code
```python
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c = 0
        for i in nums:
            a = str(i)
            if len(a) % 2 == 0:
                c += 1
        return c
