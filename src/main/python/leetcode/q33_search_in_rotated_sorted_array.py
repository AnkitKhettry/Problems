"""
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,6,7,0,1,2,4], target = 6
Output: 1

Example 3:
Input: nums = [6,7,0,1,2,4,5], target = 2
Output:

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

https://leetcode.com/problems/search-in-rotated-sorted-array/description/
"""


def search(nums, target):
    left = 0
    right = len(nums)-1
    mid = left + ((right-left)//2)

    while True:
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        if nums[mid] == target:
            return mid
        if (right-left) <= 1:
            return -1

        mid = left + ((right-left)//2)
        if nums[left] < nums[mid]:
            # Left portion is sorted
            if nums[left] < target < nums[mid]:
                # Target is in the left sorted portion
                right = mid
            else:
                # Target is not in the left sorted portion
                left = mid
        else:
            # Right portion is sorted
            if nums[mid] < target < nums[right]:
                # Target is in the right sorted portion
                left = mid
            else:
                # Target is not in the right sorted portion
                right = mid


if __name__ == "__main__":
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search([1], 0) == -1
    assert search([1], 1) == 0
