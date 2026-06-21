# Intuition
Count the number of positive and negative integers in the array and return the larger count.

# Approach
1. Initialize counters for positive and negative numbers.
2. Traverse the array.
3. If a number is positive, increment the positive counter.
4. If a number is negative, increment the negative counter.
5. Return the maximum of the two counters.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(1)

# Code
```python
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = 0
        neg = 0

        for i in nums:
            if i > 0:
                pos += 1
            elif i < 0:
                neg += 1

        return max(pos, neg)
