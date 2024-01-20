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
    running_sum_including_n = nums[0]
    for n in nums[1:]:
        if running_sum_including_n < 0:
            running_sum_including_n = n
        else:
            running_sum_including_n = n + running_sum_including_n
        max_sum = max(max_sum, running_sum_including_n)

    return max_sum


if __name__ == "__main__":
    arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4, 8]
    assert max_subarray(arr1) == 13
    arr2 = [-2, -3, -1, -5]
    assert max_subarray(arr2) == -1
