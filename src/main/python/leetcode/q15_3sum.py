"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
    such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

https://leetcode.com/problems/3sum/
"""


def threeSum(nums):
    nums.sort()
    triplets = set()
    for i in range(0, len(nums) - 2):
        if nums[i] > 0:
            break
        j = i + 1
        k = len(nums) - 1
        while j < k:
            if nums[i] + nums[j] + nums[k] == 0:
                triplets.add((nums[i], nums[j], nums[k]))
                j = j + 1
            elif nums[i] + nums[j] + nums[k] > 0:
                k = k - 1
            else:
                j = j + 1

    res_set = [list(tup) for tup in triplets]
    return res_set


if __name__ == "__main__":
    assert threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, 0, 1], [-1, -1, 2]]
    assert threeSum([0, 0, 0]) == [[0, 0, 0]]
