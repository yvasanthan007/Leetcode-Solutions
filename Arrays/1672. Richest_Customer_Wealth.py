# Intuition
Find the total wealth of each customer by summing their accounts and return the maximum wealth.

# Approach
1. Calculate the sum of each customer's accounts.
2. Find the maximum sum among all customers.
3. Return the maximum wealth.

# Complexity
- Time complexity:
    O(m × n)

- Space complexity:
    O(1)

# Code
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))
