# Intuition
We need to find the maximum profit by buying at the lowest price first and selling at a higher price later.

# Approach
1. Track the minimum price seen so far (buy price).
2. For each price, calculate profit if sold today.
3. Update maximum profit whenever a higher profit is found.
4. Continue scanning the array.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(1)

# Code
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy

        return profit
