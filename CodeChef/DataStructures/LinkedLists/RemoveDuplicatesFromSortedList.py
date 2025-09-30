'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.next = None
'''
class Solution:
    def removeDuplicates(self, head):
        # code
        if not head or not head.next:
            return head
        temp = head
        if not temp:
            return
        while temp.next:
            if temp.data == temp.next.data:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head