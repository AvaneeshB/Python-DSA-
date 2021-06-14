# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if root==None:
            return 0
        res=[]
        q=[[root,0]]
        length=1
        while(length):
            l=q.pop(0)
            length-=1
            ptr=l[0]
            res.append([ptr.val,l[1]])
            if ptr.left:
                q.append([ptr.left,l[1]+1])
                length+=1
            if ptr.right:
                q.append([ptr.right,l[1]+1])
                length+=1
        big=res[-1][1]
        ans=0
        for i in res:
            if i[1]==big:
                ans+=i[0]
        return ans
