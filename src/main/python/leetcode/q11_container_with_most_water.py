"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

https://leetcode.com/problems/container-with-most-water/submissions/1143361292/
"""


def area(r, l, arr):
    return (r - l) * min(arr[r], arr[l])


def max_area(height):
    left = 0
    right = len(height)-1
    max_area = 0
    while right > left:
        max_area = max(max_area, area(right, left, height))
        if height[right] > height[left]:
            left = left+1
        else:
            right = right - 1
    return max_area


if __name__ == "__main__":

    assert max_area([2, 1, 8, 6, 2, 5, 4, 8, 3, 5]) == 40
    assert max_area([2, 1, 8, 6, 99, 99, 4, 8, 4, 5]) == 99
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
