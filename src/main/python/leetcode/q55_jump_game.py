"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
"""


def can_jump(nums):
    current_max_jump = 1
    for i in range(len(nums)):
        if i == len(nums) - 1:
            return True
        current_max_jump = max(current_max_jump - 1, nums[i])
        if current_max_jump == 0:
            return False


if __name__ == "__main__":
    assert can_jump([2, 3, 1, 1, 4])
    assert not can_jump([3, 2, 1, 0, 4])
