# Node is defined as:
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
def solve(head):
    if not head or not head.next or not head.next.next:
        # If there are fewer than 3 nodes, there can't be any local minima or maxima
        return 0

    current = head.next  # Starting from the second node
    prev = head
    next_node = current.next
    count = 0

    while next_node:  # While we have at least three nodes to consider
        # Check if current is a local minima
        if prev.val > current.val and next_node.val > current.val:
            count += 1
        # Check if current is a local maxima
        elif prev.val < current.val and next_node.val < current.val:
            count += 1

        # Move to next set of nodes
        prev = current
        current = next_node
        next_node = next_node.next

    return count
