"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [5,2,3,4]
Output: [24,60,40,30]

[1, 5, 10, 30]
[24, 12, 4, 1]
[24, 60, 40, 30]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

https://leetcode.com/problems/product-of-array-except-self/description/
"""


def product_except_self(nums):
    forward_pass_products = []
    reverse_pass_products = []

    running_product = 1
    forward_pass_products.append(1)
    for i in range(1, len(nums)):
        running_product = running_product * nums[i-1]
        forward_pass_products.append(running_product)

    running_product = 1
    reverse_pass_products.append(1)
    for i in range(len(nums)-2, -1, -1):
        running_product = running_product * nums[i+1]
        reverse_pass_products.append(running_product)

    reverse_pass_products.reverse()

    final_products = []
    for i in range(len(forward_pass_products)):
        final_products.append(forward_pass_products[i]*reverse_pass_products[i])

    return final_products


if __name__ == "__main__":
    assert product_except_self([5, 2, 3, 4]) == [24, 60, 40, 30]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
