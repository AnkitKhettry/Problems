"""
Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

https://leetcode.com/problems/maximum-product-subarray/
"""


def maximum_subarray(nums):
    max_product = nums[0]
    current_prefix_max = 1
    current_prefix_min = 1
    # [-1,-2,-9,-6]
    size = len(nums)
    for j in range(0, size):
        if nums[j] == 0:
            current_prefix_max = 1
            current_prefix_min = 1
            max_product = max(0, max_product)
        else:
            tmp_max = current_prefix_max * nums[j]
            tmp_min = current_prefix_min * nums[j]
            current_prefix_max = max(tmp_max, tmp_min, nums[j])
            current_prefix_min = min(tmp_max, tmp_min, nums[j])
            max_product = max(current_prefix_max, max_product)

    return max_product


if __name__ == "__main__":
    assert maximum_subarray([2, 3, -2, 4]) == 6
    assert maximum_subarray([-2, 0, -1]) == 0
    assert maximum_subarray([-1, -2, -9, -6]) == 108
    
