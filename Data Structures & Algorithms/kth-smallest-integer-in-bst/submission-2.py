# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        # inorder traversal-> [2, 1, 3] -> DFS(2) -> [1, 2, 3], k = 1 -> return res[1 - 1] = res[0] = 1
        def DFS(node):
            if not node:
                return
            DFS(node.left)
            res.append(node.val)
            DFS(node.right)
        DFS(root)
        return res[k - 1]
        