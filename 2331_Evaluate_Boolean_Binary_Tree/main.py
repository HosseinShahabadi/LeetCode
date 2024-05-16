class Solution:
    def evaluateTree(self, root) -> bool:        
        match root.val:
            case 0:
                return False
            case 1:
                return True
            case 2:
                return self.evaluateTree(root.left) or self.evaluateTree(root.right)
            case _:
                return self.evaluateTree(root.left) and self.evaluateTree(root.right)