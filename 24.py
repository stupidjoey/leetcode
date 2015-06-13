# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        
        if head == None:
            return None
        
        p = head
        q = head.next
        
        if q == None:
            return p
        
        p.next = q.next
        q.next = p
        
        p.next = self.swapPairs(p.next)
        
        return q