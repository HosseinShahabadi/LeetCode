# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        def postOrder(root) -> list[int]:
            if not root:
                return []
            
            ans = [root.val]
            ans.extend(postOrder(root.right))
            ans.extend(postOrder(root.left))
            return ans


        return postOrder(root)[::-1]
