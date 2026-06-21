# Intuition
Keep all elements that are not equal to `val` at the beginning of the array.

# Approach
1. Use a pointer `i` to track the position for the next valid element.
2. Traverse the array using pointer `j`.
3. If `nums[j]` is not equal to `val`, place it at index `i`.
4. Increment `i`.
5. Return `i`, which represents the new length of the array.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(1)

# Code
```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0

        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i
