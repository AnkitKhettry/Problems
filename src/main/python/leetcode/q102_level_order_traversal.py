"""
Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).

Example:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """

    if not root:
        return []

    from collections import deque
    queue = deque()
    result = []
    queue.append(root)
    while queue:
        current_level = []
        for i in range(len(queue)):
            current_level.append(queue.popleft())
        for node in current_level:
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append([item.val for item in current_level])

    return result


if __name__ == "__main__":
    head = TreeNode(3)
    node1 = TreeNode(9)
    node2 = TreeNode(20)
    node3 = TreeNode(15)
    node4 = TreeNode(7)

    head.left = node1
    head.right = node2
    node2.left = node3
    node2.right = node4

    assert levelOrder(head) == [[3], [9,20], [15,7]]
