# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        # level by level & right child first
        def DFS(node, depth):
            if not node:
                return None
            if depth == len(res):
                res.append(node.val)
            DFS(node.right, depth + 1)
            DFS(node.left, depth + 1)
        DFS(root, 0)
        return res