class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        size = 0
        first_head = head
        while head:
            size += 1
            head = head.next

        p = size // k
        q = size % k
        ans = []
        
        for i in range(q):
            ans.append(first_head)

            for j in range(p):
                first_head = first_head.next
            
            second_head = first_head
            first_head = first_head.next
            second_head.next = None
        
        if not p:
            for i in range(k - q):
                ans.append(None)
        if not first_head:
            return ans

        for i in range(k - q):
            ans.append(first_head)

            for j in range(p - 1):
                first_head = first_head.next
            
            second_head = first_head
            first_head = first_head.next
            second_head.next = None
        
        return ans
