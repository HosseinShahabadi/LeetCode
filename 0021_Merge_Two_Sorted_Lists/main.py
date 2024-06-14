class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pointer = ans = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                ans.next = list1
                list1, ans = list1.next, list1
            else:
                ans.next = list2
                list2, ans = list2.next, list2
        
        ans.next = list1 if list1 else list2

        return pointer.next
