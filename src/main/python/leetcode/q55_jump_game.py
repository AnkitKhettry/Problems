"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
"""


def can_jump(nums):
    # Initially, goal is at the last position
    goal = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= goal:
            # If from position i, we can reach the goal, the target will now be just to
            #   reach i. So we can now update goal to i.
            goal = i

    if goal == 0:
        return True
    return False


if __name__ == "__main__":
    assert can_jump([2, 3, 1, 1, 4])
    assert not can_jump([3, 2, 1, 0, 4])
