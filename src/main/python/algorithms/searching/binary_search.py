"""
Given a sorted array, search the position of an element
"""


def binary_search(arr, start_idx, end_idx, num_to_search):

    if end_idx < start_idx:
        return -1

    mid = start_idx + int((end_idx - start_idx)/2)
    if num_to_search == arr[mid]:
        return mid

    if num_to_search > arr[mid]:
        return binary_search(arr, mid+1, end_idx, num_to_search)

    if num_to_search < arr[mid]:
        return binary_search(arr, start_idx, mid-1, num_to_search)


if __name__ == "__main__":

    print(binary_search([1, 2, 3, 4, 5], 0, 4, 4))
    print(binary_search([1, 2, 3, 4, 5], 0, 4, 6))
    print(binary_search([1, 2, 3, 4, 5], 0, 4, 1))
    print(binary_search([1, 2, 3, 4, 5], 0, 4, 5))
    print(binary_search([1, 2, 3, 4], 0, 3, 2))
    print(binary_search([1, 2, 3, 4], 0, 3, 6))
    print(binary_search([1, 2, 3, 4], 0, 3, 1))
    print(binary_search([1, 2, 3, 4], 0, 3, 4))
