class Solution:
    def possibleStringCount(self, word: str) -> int:
        root = createLL(word)
        n,tog = togetherChars(root)
        res = 1
        if n>0:
            res += sum(tog.values())
        return res

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

def traverse(root):
    c = root 
    while c:
        print(c.val,end="->")
        c = c.next

def createLL(word):
    root = ListNode(word[0])
    c = root
    for i in range(1,len(word)):
        c.next = ListNode(word[i])
        c = c.next
    return root

def togetherChars(root):
    tog = {}
    n = 0
    c = root
    while c.next:
        if c.val == c.next.val:
            if c.val not in tog.keys():
                n+=1
                tog[c.val] = 0
            tog[c.val]+=1
        c = c.next
    return n,tog