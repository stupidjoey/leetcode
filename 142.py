# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head == None:
            return None
    
        p = head
        markval = float('inf')
        while p.next != None:
            if p.val == markval:
                return p
            else:
                p.val = markval
                p = p.next
        return None
        
            