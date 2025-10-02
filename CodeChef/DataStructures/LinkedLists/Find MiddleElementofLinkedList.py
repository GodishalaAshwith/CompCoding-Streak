"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
"""

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def getMiddleElement(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast= fast.next.next
        if fast == None or fast.next == None:
            return slow.data
            
        
    
    
