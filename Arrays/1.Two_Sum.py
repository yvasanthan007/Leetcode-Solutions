# Intuition
Use a hash map to store numbers we have already seen. For each number, check if its complement (target - number) is already in the hash map.

# Approach
1. Create an empty hash map.
    2. Traverse the array.
    3. Find the complement of the current number.
    4. If the complement exists in the hash map, return their indices.
    5. Otherwise, store the current number and its index in the hash map.

# Complexity
- Time complexity:
    O(n)

- Space complexity:
    O(n)

# Code
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Hmap = {}
        n = len(nums)
        for i in range(n):
            c = target - nums[i]
            if c in Hmap:
                return [Hmap[c], i]
            Hmap[nums[i]] = i
        return []
