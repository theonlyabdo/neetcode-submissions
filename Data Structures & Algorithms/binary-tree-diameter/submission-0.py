# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        # return max height, but modify res 
        def dfs(curn):
            if not curn:
                return 0
            
            left = dfs(curn.left)
            right = dfs(curn.right)

            self.res = max(self.res,left + right)
            return 1 + max(left,right)
        
        dfs(root)
        return self.res

