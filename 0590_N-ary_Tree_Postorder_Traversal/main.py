# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: Node) -> list[int]:
        def postOrder(root) -> list[int]:
            if not root:
                return []
            
            ans = [root.val]
            for child in root.children[::-1]:
                print(f'seen child: {child.val}')
                ans.extend(postOrder(child))
            return ans


        return postOrder(root)[::-1]
        