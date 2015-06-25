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
    

    # new solution  two pointers
    def detectCycle(self, head):
        if head == None:
            return None

        fast = head
        slow = head
        
        while fast!= None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
            
        if fast == None or fast.next == None:
            return None
        
        slow = head
        while slow != fast:
            fast = fast.next
            slow = slow.next
            
        return slow


            