# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        l=[]
        if node==None:
            return node
        ptr=node
        while(ptr):
            l.append(ptr.val)
            ptr=ptr.next
        res=[]
        while(len(l)):
            if len(l)>1:
                res.append(l.pop()+l.pop(0))
            elif len(l)==1:
                res.append(l.pop())
            else:
                break
        res=res[::-1]
        ptr=node
        prev=ptr
        for i in res:
            ptr.val=i
            prev=ptr
            ptr=ptr.next
        prev.next=None
        return node
