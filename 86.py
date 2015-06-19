# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        p = head
        mark1 = 0
        mark2 = 0
        node1 = None
        node2 = None
        while p != None:
            if p.val < x:
                if mark1 == 0:
                    node1 = p
                    mark1 = 1
                    node1.next = None
            else:
                if mark2 == 0:
                    node2 = p
                    mark2 = 1
                    node2.next = None
            p = p.next
            if mark1 == 1 and mark2 == 1:
                break
        n1 = node1
        n2 = node2
        while p != None:
            if p.val <x :
                n1.next = p
                n1 = n1.next
                n1.next = None
            else:
                n2.next = p
                n2 = n2.next
                n2.next = None
            p = p.next
        
        if node1 == None:
            node1 = node2
        else:
            n1.next = node2
            
        return node1

a = ListNode(2)
b =ListNode(1)
a.next = b
sol =Solution()

node = sol.partition(a,2)
while node!=None:
    print node.val
    node = node.next
        