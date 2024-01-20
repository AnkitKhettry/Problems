"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""

def find_median_sorted_arrays(nums1, nums2):

    # https://www.youtube.com/watch?v=q6IEA26hvXc&t=20s
    ...


# 1,5,7,8,11
# 6,9,12,15,14,19,21,26,33
# half = 7
# i = 2
# j = 7 - 2 - 2 = 3


# 1,2,3,4,5
# 6,7,8,9,10




if __name__ == "__main__":
    assert find_median_sorted_arrays([1, 3], [2]) == 2
    assert find_median_sorted_arrays([1, 2], [3, 4]) == 2.5
