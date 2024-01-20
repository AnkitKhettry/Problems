"""
Given an integer array nums, return the length of the longest strictly increasing
subsequence.

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

https://leetcode.com/problems/longest-increasing-subsequence/description/
"""


def length_of_lis(nums):

    lis = [1] * len(nums)
    lis[len(nums)-1] = 1
    for i in range(len(nums) - 2, -1, -1):
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                lis[i] = max(lis[i], 1+lis[j])

    return max(lis)


if __name__ == "__main__":
    assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert length_of_lis([0, 1, 0, 3, 2, 3]) == 4
    assert length_of_lis([7, 7, 7, 7, 7, 7, 7]) == 1
