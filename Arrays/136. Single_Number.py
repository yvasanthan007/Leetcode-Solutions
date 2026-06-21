# Intuition
'''Use XOR operation. A number XOR itself becomes 0, so all duplicate numbers cancel out and only the single number remains.'''

# Approach
''' 1. Initialize a variable `r` as 0.
    2. Traverse the array.
    3. XOR each element with `r`.
    4. After all operations, `r` will contain the single number.
    5. Return `r`.'''

# Complexity
''' - Time complexity:
        O(n)

    - Space complexity:
        O(1)'''

# Code
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        r = 0
        for i in nums:
            r ^= i
        return r
