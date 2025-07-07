class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            if l1:
                value1 = l1.val
                l1 = l1.next
            else:
                value1 = 0

            if l2:
                value2 = l2.val
                l2 = l2.next
            else:
                value2 = 0

            total = value1 + value2 + carry
            digit = total % 10
            carry = total // 10

            new_node = ListNode(digit)
            current.next = new_node
            current = current.next

        return dummy.next
