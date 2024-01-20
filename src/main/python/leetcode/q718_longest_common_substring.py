"""
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

Example 1:
Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].
"""


def find_length(nums1, nums2):
    max_length = 0
    lengths_grid = [[0] * (len(nums2) + 1) for i in range(len(nums1) + 1)]

    for i in range(1, len(nums1)+1):
        for j in range(1, len(nums2) + 1):
            if nums1[i-1] == nums2[j-1]:
                lengths_grid[i][j] = lengths_grid[i - 1][j - 1] + 1
                max_length = max(max_length, lengths_grid[i][j])

    return max_length


if __name__ == "__main__":
    assert find_length([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]) == 3
    assert find_length([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]) == 5
