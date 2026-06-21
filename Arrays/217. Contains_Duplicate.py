# Intuition
If the array contains duplicates, converting it to a set will remove them. Compare the sizes of the array and the set.

# Approach
1. Convert the array into a set.
2. Compare the length of the array and the set.
3. If the lengths are different, duplicates exist.
4. Otherwise, all elements are unique.

# Complexity
- Time complexity:
    O(n)

- Space complexity:
    O(n)

# Code
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
