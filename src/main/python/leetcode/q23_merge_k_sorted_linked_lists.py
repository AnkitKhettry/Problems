"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.


Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
"""


class ListNode(object):
    # Definition for singly-linked list.

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """

    if len(lists) == 0:
        return None
    if len(lists) == 1:
        return lists[0]
    if len(lists) == 2:
        return merge_two_lists(lists[0], lists[1])

    mid = int(len(lists) / 2)

    return merge_two_lists(
        mergeKLists(lists[:mid]), mergeKLists(lists[mid:])
    )


def merge_two_lists(list1, list2):

    if not list1:
        return list2
    if not list2:
        return list1

    merged_cur = ListNode()

    merged_head = merged_cur

    while list1 and list2:
        if list1.val < list2.val:
            merged_cur.next = list1
            list1 = list1.next
        else:
            merged_cur.next = list2
            list2 = list2.next

        merged_cur = merged_cur.next

    if list1:
        merged_cur.next = list1
    else:
        merged_cur.next = list2
    return merged_head.next


if __name__ == "__main__":

    list_1 = ListNode(1)
    list_1.next = ListNode(4)
    list_1.next.next = ListNode(5)

    list_2 = ListNode(1)
    list_2.next = ListNode(3)
    list_2.next.next = ListNode(4)

    list_3 = ListNode(2)
    list_3.next = ListNode(6)

    merged_list = mergeKLists([list_1, list_2, list_3])

    assert merged_list.val == 1
    merged_list = merged_list.next
    assert merged_list.val == 1
    merged_list = merged_list.next
    assert merged_list.val == 2
    merged_list = merged_list.next
    assert merged_list.val == 3
    merged_list = merged_list.next
    assert merged_list.val == 4
    merged_list = merged_list.next
    assert merged_list.val == 4
    merged_list = merged_list.next
    assert merged_list.val == 5
    merged_list = merged_list.next
    assert merged_list.val == 6
    merged_list = merged_list.next
    assert not merged_list
