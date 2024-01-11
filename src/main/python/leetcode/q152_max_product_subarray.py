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
    max_product = max(nums)
    running_max_product = 1
    running_min_product = 1

    for n in nums:
        if n == 0:
            running_max_product, running_min_product = 1, 1
        else:
            tmp_max_product = running_max_product * n
            tmp_min_product = running_min_product * n
            running_max_product = max(n, tmp_max_product, tmp_min_product)
            running_min_product = min(n, tmp_max_product, tmp_min_product)
            max_product = max(max_product, running_max_product)

    return max_product


if __name__ == "__main__":
    assert maximum_subarray([2,3,-2,4]) == 6
    assert maximum_subarray([-2,0,-1]) == 0
