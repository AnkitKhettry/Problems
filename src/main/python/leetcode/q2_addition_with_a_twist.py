"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
 and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

    def get_str(self):
        if self.next is None:
            return str(self.val)
        return f"{str(self.val)} -> {self.next.get_str()}"


def get_num(node, multiplier):
    if node is None:
        return 0
    return (multiplier * node.val) + get_num(node.next, multiplier * 10)


def create_linked_list_from_number(remaining_number):
    if int(remaining_number / 10) == 0:
        return ListNode(remaining_number)
    return ListNode(remaining_number % 10, create_linked_list_from_number(int(remaining_number / 10)))


def add_two_numbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    first_num = get_num(l1, 1)
    second_num = get_num(l2, 1)
    total_sum = first_num + second_num

    return create_linked_list_from_number(total_sum)


if __name__ == "__main__":
    # First number: 342
    node1 = ListNode(2)
    node2 = ListNode(4)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3

    # Second number: 465
    node4 = ListNode(5)
    node5 = ListNode(6)
    node6 = ListNode(4)
    node4.next = node5
    node5.next = node6

    reqd_sum = add_two_numbers(node1, node4)
    print(reqd_sum.get_str())
