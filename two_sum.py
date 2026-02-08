# LeetCode 1: Two Sum
# Approach: Hash Map
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in seen:
                return [seen[needed], i]
            seen[nums[i]] = i
