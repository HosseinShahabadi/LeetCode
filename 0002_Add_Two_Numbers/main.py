class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1pointer = l1
        l2pointer = l2

        l1_list = []
        l2_list = []

        while l1pointer:
            l1_list.append(l1pointer.val)
            l1pointer = l1pointer.next
        
        while l2pointer:
            l2_list.append(l2pointer.val)
            l2pointer = l2pointer.next
        
        l1_list.reverse()
        l2_list.reverse()
        
        value = int(''.join(str(v) for v in l1_list)) + int(''.join(str(v) for v in l2_list))
        output = [int(x) for x in str(value)]
        
        head = list_node = ListNode(output.pop())

        output.reverse()

        for i in output:
            list_node.next = ListNode(i)
            list_node = list_node.next

        return head
