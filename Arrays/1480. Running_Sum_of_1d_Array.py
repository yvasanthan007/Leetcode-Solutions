# Intuition
Keep adding the current number to a running total and store the result in a new array.

# Approach
1. Initialize an empty array and a variable for the running sum.
2. Traverse the array.
3. Add the current element to the running sum.
4. Append the running sum to the result array.
5. Return the result array.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(n)

# Code
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = []
        a = 0

        for i in range(len(nums)):
            a += nums[i]
            s.append(a)

        return s
