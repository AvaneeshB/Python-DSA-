# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, target):
      if root==None:
          return root
      queue=[root]
      while(len(queue)):
          ptr=queue.pop(0)
          print(ptr.val,end=" ")
          if ptr.left:
              q.append(ptr.left)
          if ptr.right:
              q.append(ptr.right)
