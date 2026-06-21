# Intuition
Use two pointers at both ends and calculate the area formed. Move the pointer with the smaller height to try finding a larger area.

# Approach
1. Place one pointer at the beginning and one at the end.
2. Calculate the area using the current width and the smaller height.
3. Update the maximum area if needed.
4. Move the pointer with the smaller height inward.
5. Repeat until the pointers meet.
6. Return the maximum area found.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(1)

# Code
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            h = min(height[left], height[right])

            max_area = max(max_area, width * h)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
