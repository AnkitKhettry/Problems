class Node:
    # Node for a doubly linked list
    def __init__(self, key=None, val=None, left=None, right=None):
        self.key = key
        self.val = val


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}

        # Doubly linked list to keep track of LRU nodes
        self.head = Node()
        self.tail = Node()
        self.head.right = self.tail
        self.tail.left = self.head

    def bring_node_closest_to_tail(self, node):
        # HEAD <-> 1 <-> 2 <-> TAIL
        # HEAD <-> 2 <-> 1 <-> TAIL

        # HEAD <-> 2 <-> TAIL
        left_node = node.left
        right_node = node.right
        left_node.right = right_node
        right_node.left = left_node
        last_node = self.tail.left
        last_node.right = node
        self.tail.left = node
        node.left = last_node
        node.right = self.tail

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.cache.get(key)
        if node:
            # Key exists in cache.
            # Remove it from the linkedlist and bring it closest to the tail.
            self.bring_node_closest_to_tail(node)
            return node.val
        else:
            # Key doesnt exist in cache
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = self.cache.get(key)
        if node:
            # Key already exists in cache.
            # Update the value of the node and bring it closest to tail
            node.val = value
            self.bring_node_closest_to_tail(node)
        else:
            # Key doesnt exist in cache
            # Create the node
            node = Node(key, value)
            if self.capacity == len(self.cache):
                # HEAD <-> 2 <-> 1 <-> TAIL
                # Cache has reached max capacity.
                # Remove least recently used node from the list and the key from the cache
                key_to_remove = self.head.right.key
                self.cache.pop(key_to_remove)
                self.head.right = self.head.right.right
                self.head.right.left = self.head
                # Now insert the node into the end
                last_node = self.tail.left
                last_node.right = node
                self.tail.left = node
                node.right = self.tail
                node.left = last_node
            else:
                # Cache has capacity. Just insert node in the end
                last_node = self.tail.left
                last_node.right = node
                self.tail.left = node
                node.right = self.tail
                node.left = last_node
            self.cache[key] = node


if __name__ == "__main__":
    cache1 = LRUCache(2)
    cache1.put(1, 1)
    cache1.put(2, 2)
    assert cache1.get(1) == 1
    cache1.put(3, 3)
    assert cache1.get(2) == -1
    cache1.put(4, 4)
    assert cache1.get(1) == -1
    assert cache1.get(3) == 3
    assert cache1.get(4) == 4

    cache2 = LRUCache(1)
    cache2.put(2, 1)
    assert cache2.get(2) == 1
    cache2.put(3, 2)
    assert cache2.get(2) == -1
    assert cache2.get(3) == 2




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)