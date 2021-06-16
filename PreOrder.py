# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root==None:
            return root
        s=[]
        res=[]
        ptr=root
        while(1):
            if ptr:
                s.append(ptr)
                res.append(ptr.val)
                ptr=ptr.left
            elif len(s):
                ptr=s.pop()
                ptr=ptr.right
            else:
                return res
