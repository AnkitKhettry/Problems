"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

-2, 1, -3, 4, -1, 2, 1, -5, 4
"""


def max_subarray_quadratic(nums):

    max_sum = nums[0]
    idx_i = 0
    idx_j = 0

    size = len(nums)

    for i in range(0, size):
        total = 0
        for j in range(i, size):
            total = total + nums[j]
            if total > max_sum:
                max_sum = total
                idx_j = j
                idx_i = j-i

    print(f"max_sum: {max_sum}, i: {idx_i}, j: {idx_j}")
    return max_sum





def max_subarray(nums):
    max_sum = nums[0]
    prev_max_sum = nums[0]

    for num in nums[1:]:
        if num + prev_max_sum > num:
            prev_max_sum = num + prev_max_sum
        else:
            prev_max_sum = num
        max_sum = max(prev_max_sum, max_sum)

    return max_sum


if __name__ == "__main__":
    arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4, 8]
    assert max_subarray(arr1) == 13
    arr2 = [-2, -3, -1, -5]
    assert max_subarray(arr2) == -1
