# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
        if head == None:
            return None
        nums = []
        while head != None:
            nums.append(head.val)
            head = head.next
        root = self.rec_buildBST(nums)
        return root
    def rec_buildBST(self, nums):
        n = len(nums)
        if n == 0:
            return None
        if n == 1:
            return TreeNode(nums[0])
        mid = n/2
        root = TreeNode(nums[mid])
        root.left = self.rec_buildBST(nums[0:mid])
        root.right = self.rec_buildBST(nums[mid+1:])
        
        return root
        
        
        
        