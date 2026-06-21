# Intuition
'''Move all non-zero elements to the front while keeping their order. The remaining positions will automatically contain zeros after swapping.'''

# Approach
''' 1. Use a pointer `left` to track the position for the next non-zero element.
    2. Traverse the array.
    3. If the current element is non-zero, swap it with the element at `left`.
    4. Increment `left`.
    5. Continue until the end of the array.'''

# Complexity
''' - Time complexity:
        O(n)

    - Space complexity:
        O(1)'''

# Code
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
        return nums
