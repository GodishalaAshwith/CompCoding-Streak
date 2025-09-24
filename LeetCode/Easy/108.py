class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def makeBST(i, j):
            if i <= j:
                mid = (i + j) // 2
                node = TreeNode(nums[mid])
                node.left = makeBST(i, mid - 1)
                node.right = makeBST(mid + 1, j)
                return node

        return makeBST(0, len(nums) - 1)