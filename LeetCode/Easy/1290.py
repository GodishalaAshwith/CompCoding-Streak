# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        binary = []
        c = head
        while c:
            binary.append(str(c.val))
            c = c.next
        binary_string = "".join(binary)
        return int(binary_string,2)