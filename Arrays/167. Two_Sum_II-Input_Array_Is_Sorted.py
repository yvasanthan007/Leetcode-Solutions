# Intuition
Since the array is sorted, use two pointers from both ends to find the target sum efficiently.

# Approach
1. Initialize two pointers: left at the beginning and right at the end.
2. Calculate the sum of the two numbers.
3. If the sum equals the target, return their 1-based indices.
4. If the sum is smaller than the target, move left forward.
5. If the sum is greater than the target, move right backward.
6. Repeat until the target is found.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(1)

# Code
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
