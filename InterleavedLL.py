# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, l0, l1):
        first = l0
        sec = l1
        # till any of the pointer exists
        while first and sec:
            # storing the next pointers of both lists
            first_next = first.next
            second_next = sec.next
            # now check if next node exists in the first list
            if first_next:
                first.next = sec
                sec.next = first_next
                first = first_next
                sec = second_next
            # otherwise just appendind the first to second and return
            else:
                first.next = sec
                return l0
        if l0:
            return l0
        else:
            return l1
