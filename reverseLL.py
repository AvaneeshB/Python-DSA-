# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def solve(self, node):
        head, prev = node, None
        while head:
            head.next, prev, head = prev, head, head.next
        return prev
