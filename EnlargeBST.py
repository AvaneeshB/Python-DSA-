# Given a binary search tree root, replace every node's value v by its value plus the sum of all other values in the tree that are greater than v.

class Solution:
    def solve(self, root):
        if root==None:
            return root
        s=[]    
        res=[]    
        ptr=root
        while(1):
            if ptr:
                s.append(ptr)
                ptr=ptr.left
            elif len(s):
                ptr=s.pop()
                res.append(ptr.val)
                ptr=ptr.right
            else:
                break
        res=res[::-1]
        summer=res[0]
        for i in range(len(res)):
            if i==0:
                continue
            res[i],summer=(res[i]+summer),res[i]+summer
        s=[]      
        ptr=root
        while(1):
            if ptr:
                s.append(ptr)
                ptr=ptr.left
            elif len(s):
                ptr=s.pop()
                ptr.val=res.pop()
                ptr=ptr.right
            else:
                return root
