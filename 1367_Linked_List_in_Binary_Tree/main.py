class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(h, r):
            if not h:
                return True
            if not r:
                return False
            
            if r.val == h.val:
                return dfs(h.next, r.left) or dfs(h.next, r.right)
            return False

        def traverse_tree(r):
            if not r:
                return False
            
            return dfs(head, r) or traverse_tree(r.left) or traverse_tree(r.right)

        return traverse_tree(root)
