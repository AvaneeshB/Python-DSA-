def travel(root,k,d):
    if not root:
        return 
    if k not in d:
        d[k]=0
    d[k]+=root.val
    travel(root.left,k+1,d)
    travel(root.right,k,d)


class Solution:
    def solve(self, root):
        d={}
        travel(root,0,d)
        res=list(d.values())     
        return res
