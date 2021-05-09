# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        return (self.flip(None, head))
        
    def flip(self, prev, node):
        if node.next == None:
            node.next = prev
            return node
        nextnode =node.next
        node.next = prev
        return self.flip(node, nextnode)

    def reverseList(self, head):  # Iterative
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev