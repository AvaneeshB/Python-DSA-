# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, target):
     if root==None:
        return 0
     stack=[]
     ptr=root
     count=0
     while(1):
        if ptr:
          stack.append(ptr)
          ptr=ptr.left
        elif (len(stack)):
          ptr=stack.pop()
          count+=1
          ptr=ptr.right
        else:
          break
     return count 
