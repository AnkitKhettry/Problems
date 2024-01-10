class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

    def get_str(self):
        if self.next is None:
            return str(self.val)
        return f"{str(self.val)} -> {self.next.get_str()}"


def reverse_linked_list(head_node):

    prev_node = None
    curr_node = head_node
    while curr_node.next is not None:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    curr_node.next = prev_node

    return curr_node


if __name__ == "__main__":
    """
    Reverse a linked list.
    """
    node1 = ListNode(2)
    node2 = ListNode(4)
    node3 = ListNode(3)
    node4 = ListNode(1)
    node5 = ListNode(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    print(node1.get_str())

    new_head = reverse_linked_list(node1)

    print(new_head.get_str())
