# Intuition
Use XOR to cancel out all matching numbers. The remaining value will be the missing number.

# Approach
1. Initialize a variable with the length of the array.
2. XOR it with all indices and all numbers in the array.
3. Since equal numbers cancel out, only the missing number remains.
4. Return the result.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(1)

# Code
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = len(nums)

        for i in range(len(nums)):
            xor ^= i ^ nums[i]

        return xor
