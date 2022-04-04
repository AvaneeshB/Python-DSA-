''' Given a binary tree root, 
    return the same tree except every node's value
    is replaced by its original value plus all of 
    the sums of its left and right subtrees.
'''

def dfs(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return root.val
    left=dfs(root.left)
    right=dfs(root.right)
    root.val=left+right+root.val
    return root.val


class Solution:
    def solve(self, root):
        if not root:
            return root
        dfs(root)
        return root
