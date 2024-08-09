"""
Given a sorted array, search the position of an element
"""


def binary_search(arr, num_to_search, start):

    if num_to_search > arr[len(arr)-1] or num_to_search < arr[0]:
        return -1
    mid = int(len(arr)/2)

    if num_to_search == arr[mid]:
        return start + mid
    if num_to_search < arr[mid]:
        return binary_search(arr[:mid], num_to_search, start)
    else:
        return binary_search(arr[mid:], num_to_search, start+mid)


if __name__ == "__main__":

    print(binary_search([1, 2, 3, 4, 5], 6, 0))
    print(binary_search([1, 2, 3, 4, 5], 0, 0))
    print(binary_search([1, 2, 3, 4, 5], 1, 0))
    print(binary_search([1, 2, 3, 4, 5], 3, 0))
    print(binary_search([1, 2, 3, 4, 5], 4, 0))
    print(binary_search([1, 2, 3, 4, 5], 5, 0))
    print(binary_search([1, 2, 3, 4], 1, 0))
    print(binary_search([1, 2, 3, 4], 2, 0))
    print(binary_search([1, 2, 3, 4], 3, 0))
    print(binary_search([1, 2, 3, 4], 4, 0))
