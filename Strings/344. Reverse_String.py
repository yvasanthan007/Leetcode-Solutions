# Intuition
'''Use two pointers, one at the beginning and one at the end. Swap the characters and move both pointers toward the center.'''

# Approach
''' 1. Initialize two pointers: left at the start and right at the end.
    2. Swap the characters at both pointers.
    3. Move left forward and right backward.
    4. Repeat until the pointers meet.'''

# Complexity
''' - Time complexity:
        O(n)

    - Space complexity:
        O(1)'''

# Code
class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s) - 1

        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s
