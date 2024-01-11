"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

https://leetcode.com/problems/3sum/
"""


def three_sum(nums):

    res_set = []
    nums.sort()

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i+1
        right = len(nums)-1
        while left < right:
            if left > i+1 and nums[left] == nums[left-1]:
                left = left+1
                continue
            curr_sum = nums[i] + nums[left] + nums[right]
            if curr_sum > 0:
                right = right - 1
            elif curr_sum < 0:
                left = left + 1
            else:
                res_set.append([nums[i], nums[left], nums[right]])
                left = left+1

    return res_set


if __name__ == "__main__":
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]
