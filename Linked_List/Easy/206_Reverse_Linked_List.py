class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev_node, curr = None, head
        while curr:
            next_node = curr.next
            curr.next = prev_node

            prev_node = curr
            curr = next_node
        return prev_node
