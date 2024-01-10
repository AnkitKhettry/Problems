"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

-2, 1, -3, 4, -1, 2, 1, -5, 4
"""


def max_subarray(nums):

    # Smallest python integer:
    max_sum = float('-inf')
    max_sum_till_n = max_sum

    for n in nums:
        max_sum_till_n = max(n, max_sum_till_n + n)
        max_sum = max(max_sum, max_sum_till_n)

    print(max_sum)

    return max_sum


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


if __name__ == "__main__":
    arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_subarray(arr1)
    arr2 = [-2, -3, -1, -5]
    max_subarray(arr2)
