# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(node, arr):
    if node is None:
        return arr
    else:
        arr = inorder_traversal(node.left, arr)
        arr.append(node.val)
        arr = inorder_traversal(node.right, arr)
        return arr


def preorder_traversal(node, arr):
    if node is None:
        return arr
    else:
        arr.append(node.val)
        arr = preorder_traversal(node.left, arr)
        arr = preorder_traversal(node.right, arr)
        return arr


def postorder_traversal(node, arr):
    if node is None:
        return arr
    else:
        arr = postorder_traversal(node.left, arr)
        arr = postorder_traversal(node.right, arr)
        arr.append(node.val)
        return arr


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)

    node1.right = node2
    node2.left = node3
    inorder_arr = inorder_traversal(node1, [])
    print(inorder_arr)
    preorder_arr = preorder_traversal(node1, [])
    print(preorder_arr)
    postorder_arr = postorder_traversal(node1, [])
    print(postorder_arr)
