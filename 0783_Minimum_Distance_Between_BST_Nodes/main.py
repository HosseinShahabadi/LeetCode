class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def getSortedTree(root: Optional[TreeNode]) -> list:
            out = []
            if root.left:
                out.extend(getSortedTree(root.left))
            out.append(root.val)
            if root.right:
                out.extend(getSortedTree(root.right))
            return out

        tree = getSortedTree(root)
        ans = float('inf')
        for i in range(1, len(tree)):
            if abs(tree[i] - tree[i-1]) < ans:
                ans = abs(tree[i] - tree[i-1])

        return ans
