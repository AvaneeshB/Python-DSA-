# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root==None:
            return root
        q=[root]
        l=1
        while(l):
            ptr=q.pop(0)
            l-=1
            if ptr:
                ptr.left,ptr.right=ptr.right,ptr.left
            if ptr.left:
                q.append(ptr.left)
                l+=1
            if ptr.right:
                q.append(ptr.right)
                l+=1
        return root
