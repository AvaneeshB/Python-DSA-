def newNode(arg):
    ptr=LLNode(arg,None)
    return ptr
class Solution:
    def solve(self, root):
        if not root:
            return root
        head=newNode(-1)
        prev=head
        q=[root]
        while(len(q)):
            ptr=q.pop(0)
            node=newNode(ptr.val)
            prev.next=node
            prev=node
            if ptr.left:
                q.append(ptr.left)
            if ptr.right:
                q.append(ptr.right)
        return head.next
