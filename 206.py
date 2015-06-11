# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        
        pre_node = None
        p = head
        while p != None:
            next_node = p.next
            p.next = pre_node
            pre_node = p
            p = next_node
            
        return pre_node