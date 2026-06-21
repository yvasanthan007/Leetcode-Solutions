# Intuition
Square each number and sort the resulting values to get the array in non-decreasing order.

# Approach
1. Create an empty array.
2. Traverse the input array.
3. Square each element and add it to the new array.
4. Sort the new array.
5. Return the sorted array.

# Complexity
- Time complexity:
O(n log n)

- Space complexity:
O(n)

# Code
```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = []

        for i in nums:
            arr.append(i * i)

        arr.sort()
        return arr
