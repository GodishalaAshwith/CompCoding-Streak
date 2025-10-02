'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
class Solution:
    # Function to detect the cycle and return the node where the cycle begins
    def detectCycle(self, head):
        # If the linked list is empty or has only one node, there's no cycle
        if head is None or head.next is None:
            return None

        # Initialize two pointers for the Floyd's cycle detection algorithm
        slow = head
        fast = head

        # Traverse the list
        while fast and fast.next:
            slow = slow.next         # Move slow pointer by one step
            fast = fast.next.next    # Move fast pointer by two steps

            # Check if the pointers meet inside the list
            if slow == fast:
                # Cycle detected, now find the start of the cycle
                slow = head         # Reset slow to the beginning

                # Move slow and fast one step at a time
                while slow != fast: 
                    slow = slow.next
                    fast = fast.next

                return slow         # The node where slow and fast meet is the start of the cycle

        # No cycle detected
        return None
