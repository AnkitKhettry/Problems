"""
Rearrange array such that arr[i] >= arr[j] if i is even and arr[i]<=arr[j] if i is odd and j < i
  Given an array of n elements. Our task is to write a program to rearrange the array such that elements at even
  positions are greater than all elements before it and elements at odd positions are less than all elements before it.
Example:
  Input : arr[] = {1, 2, 3, 4, 5, 6, 7}
  Output : 4 5 3 6 2 7 1
"""


def rearrange_array(arr: list):
    """
    Given an array, rearranges it, such that arr[i] >= arr[j] if i is even and arr[i]<=arr[j] if i is odd and j < i
    Args:
        arr: List
            Array of integers
    Returns:
        list
    """
    arr_size = len(arr)
    # + O(n log n) time complexity, + O(n) space complexity
    sorted_arr = sorted(arr)

    # + O(n) time complexity
    for i in range(arr_size):
        if i % 2 == 0:
            arr[i] = sorted_arr[arr_size-i-1]
        else:
            arr[i] = sorted_arr[i]

    return arr


if __name__ == '__main__':

    new_arr = rearrange_array([5, 23, 7, 54, 9, 54])
    print(new_arr)
