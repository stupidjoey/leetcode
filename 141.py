# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head == None:
            return False
        
        head.val = 'A'
        p = head.next
        
        while p != None:
            if p.val == 'A':
                return True
            else:
                p.val = 'A'
                p = p.next
            
        return False
            