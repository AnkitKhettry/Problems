"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true

Example 2:

Input: nums = [1,2,3,4]
Output: false

https://leetcode.com/problems/contains-duplicate/
"""


def contains_duplicate(nums):
    set_of_nums = set()
    for i in range(len(nums)):
        if nums[i] not in set_of_nums:
            set_of_nums.add(nums[i])
        else:
            return True
    return False


if __name__ == "__main__":
    assert contains_duplicate([1, 2, 3, 1]) == True
    assert contains_duplicate([1, 2, 3, 4]) == False