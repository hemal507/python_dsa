# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next :
            return head
        slow = head
        fast = head.next
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left, right)
    def merge(self, l, r):
        dummy = ListNode(0)
        tmp = dummy
        while l and r :
            if l.val < r.val :
                tmp.next = l
                l = l.next
            else :
                tmp.next = r
                r = r.next
            tmp = tmp.next
        tmp.next = l or r 
        return dummy.next