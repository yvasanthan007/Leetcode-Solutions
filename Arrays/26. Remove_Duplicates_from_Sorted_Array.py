# Intuition
Since the array is sorted, duplicates are adjacent. Keep only unique elements and place them at the front of the array.

# Approach
1. Use a pointer `k` to track the position of the next unique element.
2. Traverse the array starting from index 1.
3. If the current element is different from the previous unique element, place it at index `k`.
4. Increment `k`.
5. Return `k`, which represents the number of unique elements.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(1)

# Code
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k
