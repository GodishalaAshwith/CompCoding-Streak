# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        def get_tree(node):
            if not node:
                return [None]
            t = []
            t.append(node.val)
            l = get_tree(node.left)
            r = get_tree(node.right)
            t.extend(l)
            t.extend(r)
            return t
        return get_tree(p) == get_tree(q)