# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if root==None:
            return root
        q=[[root,0]]
        chk=[]
        t=1
        while(t):
            l=q.pop(0)
            t-=1
            ptr=l[0]
            if ptr.left:
                q.append([ptr.left,l[1]+1])
                t+=1
            if ptr.right:
                q.append([ptr.right,l[1]+1])
                t+=1
            if ptr.left==None and ptr.right==None:
                chk.append(l[1])
        s=list(set(chk))
        if len(s)==1:
            return True
        return False
