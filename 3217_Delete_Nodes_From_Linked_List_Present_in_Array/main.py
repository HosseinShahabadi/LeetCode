class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        values_to_remove = set(nums)
        while head.val in values_to_remove:
            head = head.next
        
        root = head
        while head.next:
            if head.next.val in values_to_remove:
                head.next = head.next.next
            else:
                head = head.next

        return root
