# Intuition
Count the frequency of each number and return the one that appears more than n/2 times.

# Approach
1. Create a hash map to store frequencies.
2. Traverse the array and count occurrences of each number.
3. Traverse the hash map.
4. Return the number whose frequency is greater than n/2.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(n)

# Code
```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num, count in freq.items():
            if count > len(nums) // 2:
                return num
