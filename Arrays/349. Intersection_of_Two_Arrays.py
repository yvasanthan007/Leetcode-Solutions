# Intuition
Convert both arrays into sets and find the common elements between them.

# Approach
1. Convert `nums1` and `nums2` into sets to remove duplicates.
2. Find the intersection of the two sets.
3. Convert the result back to a list.
4. Return the list.

# Complexity
- Time complexity:
O(n + m)

- Space complexity:
O(n + m)

# Code
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        return list(nums1 & nums2)
