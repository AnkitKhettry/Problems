"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [6,7,0,1,2,4,5]
Output: 7
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 2 times.

Example 2:
Input: nums = [3,4,5,6,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""


def find_min(nums):
    first = 0
    last = len(nums) - 1
    if len(nums) == 1:
        return nums[0]
    if nums[first] < nums[last]:
        # Array is already sorted. Return nums[first]
        return nums[first]

    while True:
        if (last-first) == 1:
            return nums[last]
        mid = first + ((last - first) // 2)
        if nums[first] < nums[mid]:
            first = mid
        else:
            last = mid


if __name__ == "__main__":
    assert find_min([3, 4, 5, 1, 2]) == 1
    assert find_min([6, 7, 0, 1, 2, 4, 5]) == 0
