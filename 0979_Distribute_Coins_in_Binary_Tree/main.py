class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root is None:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            nonlocal ans
            ans += (abs(left) + abs(right))
            return left + right + root.val - 1

        ans = 0
        dfs(root)
        return ans
        