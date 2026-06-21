# Intuition
Since both arrays are already sorted, we can merge them from the back to avoid overwriting elements in nums1.

# Approach
1. Use three pointers:
   - i at end of nums1’s valid elements
   - j at end of nums2
   - k at the end of nums1
2. Compare elements from the back.
3. Place the larger element at position k.
4. Move pointers accordingly.
5. If any elements remain in nums2, copy them.

# Complexity
- Time complexity:
O(m + n)

- Space complexity:
O(1)

# Code
```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
