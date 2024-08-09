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


def search_recursive(nums, target, start_idx):
    if len(nums) == 1 and nums[0] != target:
        return -1
    last = len(nums) - 1
    mid = int(last / 2)
    if nums[mid] == target:
        return start_idx + mid
    if nums[mid + 1] <= nums[last]:
        # Right half is sorted
        if nums[mid + 1] <= target <= nums[last]:
            # Target belongs in the right half
            return search_recursive(nums[mid + 1:], target, start_idx + mid + 1)
        else:
            # Target doesn't belong in the right half
            return search_recursive(nums[:mid + 1], target, start_idx)
    else:
        # Left half is sorted
        if nums[0] <= target <= nums[mid]:
            # Target belongs in the left half
            return search_recursive(nums[:mid + 1], target, start_idx)
        else:
            # Target doesn't belong in the left half
            return search_recursive(nums[mid + 1:], target, start_idx + mid + 1)


def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    return search_recursive(nums, target, 0)


if __name__ == "__main__":
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search([1, 3], 0) == -1
    assert search([1], 0) == -1
    assert search([1], 1) == 0
    assert (search([1, 3], 0)) == -1
    print("Tests complete")
