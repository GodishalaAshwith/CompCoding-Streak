Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def length(head):
    l = 0
    curr = head
    while curr:
        l+=1
        curr = curr.next
    return l

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = length(head)
        m = l//2
        
        i = 0
        curr = head
        while curr:
            if i == m:
                return curr
            i+=1
            curr = curr.next
        return head