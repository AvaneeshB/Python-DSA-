class Solution:
    def solve(self, root0, root1):
        if not root0 and root1:
            return False
        if not root1 and root0:
            return False
        if not root0 and not root1:
            return True
        a = [root0]
        b = [root1]
        while len(a):
            ptr0 = a.pop()
            ptr1 = b.pop()
            if ptr0.val!=ptr1.val:
                return False
            if ptr0.left:
                if ptr1.left:
                    a.append(ptr0.left)
                    b.append(ptr1.left)
                else:
                    return False
            if ptr0.right:
                if ptr1.right:
                    a.append(ptr0.right)
                    b.append(ptr1.right)
                else:
                    return False
        return True
                    
