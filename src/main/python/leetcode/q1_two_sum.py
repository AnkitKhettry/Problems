"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
  Given nums = [2, 7, 11, 15], target = 9,
  Because nums[0] + nums[1] = 2 + 7 = 9,
  return [0, 1].
"""


def two_sum_brute_force(nums, target):

    size = len(nums)
    for i in range(0, size-1):
        for j in range(i+1, size):
            if nums[i] + nums[j] == target:
                return i, j

    return -1, -1


def two_sum(nums, target):
    num_dict = {}
    for i in range(len(nums)):
        if target - nums[i] in num_dict:
            return i, num_dict[target - nums[i]]
        num_dict[nums[i]] = i


if __name__ == "__main__":
    #print(binary_search([1,2,3,4,6], 6))
    print(two_sum([1, 5, 7, 3, 8], 13))
