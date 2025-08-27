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
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    start = 0
    end = len(nums) - 1
    while True:
        if start == end and nums[start] != target:
            return -1
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        mid = int((start + end) / 2)
        if nums[mid] == target:
            return mid
        if nums[mid+1] == target:
            return mid+1
        if nums[start] <= target <= nums[mid]:
            end = mid
        elif nums[mid+1] <= target <= nums[end]:
            start = mid + 1
        elif nums[start] > nums[mid]:
            end = mid
        else:
            start = mid + 1


if __name__ == "__main__":
    assert search([4, 5, 6, 7, 8, 1, 2, 3], 2) == 6
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search([4, 5, 6, 7, 0, 1, 2], 1) == 5
    assert search([1, 2, 3, 4, 5, 6], 5) == 4
    assert search([1, 2, 3, 4, 5, 6], 1) == 0
    assert search([1, 2, 3, 4, 5, 6], 6) == 5
    assert search([1, 2, 3, 4, 5, 6], 6) == 5
    assert search([6, 1, 2, 3, 4, 5], 6) == 0
    assert search([6, 1, 2, 3, 4, 5], 1) == 1
    assert search([3, 4, 5, 6, 1, 2], 1) == 4
    assert search([2, 3, 4, 5, 6, 1], 6) == 4
    assert search([0, 1], 0) == 0
    assert search([0, 1], 1) == 1
    assert search([0, 1], 2) == -1
    assert search([1, 0], 0) == 1
    assert search([1, 0], 1) == 0
    assert search([1, 0], 2) == -1
    assert search([0], 0) == 0
    assert search([0], 1) == -1
    assert(search([5, 1, 2, 3, 4], 1)) == 1

    print("Tests complete")
