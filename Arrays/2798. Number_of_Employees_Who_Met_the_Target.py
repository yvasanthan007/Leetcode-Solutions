# Intuition
Count how many employees worked at least the target number of hours.

# Approach
1. Initialize a counter.
2. Traverse the list of hours.
3. For each employee, check if hours >= target.
4. If yes, increment the counter.
5. Return the final count.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(1)

# Code
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        c = 0
        for i in hours:
            if i >= target:
                c += 1
        return c
