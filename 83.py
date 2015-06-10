# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head
            
        pre_node = head
        pre_val = head.val
        p = head.next
        while p != None:
            if p.val != pre_val:
                pre_node.next = p
                pre_node = p
                pre_val = p.val
            else:
                pre_node.next = None
            p = p.next
        return head
                
        