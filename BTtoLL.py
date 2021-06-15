# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, root):
        if root==None:
            return root
        head=LLNode(-1)
        head.next=None
        curr=head
        s=[]
        ptr=root
        while(1):
            if ptr:
                s.append(ptr)
                ptr=ptr.left
            elif(len(s)):
                ptr=s.pop()
                node=LLNode(ptr.val)
                node.next=curr.next
                curr.next=node
                curr=node
                ptr=ptr.right
            else:
                break
        return head.next
