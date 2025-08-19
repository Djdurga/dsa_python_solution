'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)   
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.containsDuplicate([1,2,3,1]))  # Should print: True
    print(s.containsDuplicate([1,2,3,4]))  # Should print: False
    print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))  # Should print: True