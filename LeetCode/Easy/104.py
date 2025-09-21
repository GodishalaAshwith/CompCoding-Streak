# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:  # Checking if the root is empty
            return 0

        def m(node):  # searching the length of each node
            if not node:  # we reached the end
                return 0
            l = m(node.left)  # doing dfs for the left side
            r = m(node.right)  # taking length of right now
            return 1 + max(l, r)  # this returns the max length

        return m(root)  # gives us the max length of tree

