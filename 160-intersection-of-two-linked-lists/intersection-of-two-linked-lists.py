# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dummya = headA
        dummyb = headB

        while dummya != dummyb :
            dummya = dummya.next if dummya else headB
            dummyb = dummyb.next if dummyb else headA
        return dummya