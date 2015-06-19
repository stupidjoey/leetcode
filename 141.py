# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    
    # original solution 
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
    
    # new solution  fast and slow runners
    def hasCycle(self, head):
        if head == None:
            return False
        
        fast = head
        slow = head
        
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        
        return False
        
    
            