def newNode(arg):
    node=LLNode(arg,None)
    return node

class Solution:
    def solve(self, l0, l1):

        a=""
        b=""
        ptr=l0
        while(ptr):
            a+=str(ptr.val)
            ptr=ptr.next
        a=a[::-1]
        ptr=l1
        while(ptr):
            b+=str(ptr.val)
            ptr=ptr.next
        b=b[::-1]
        res=str(int(a)+int(b))
        res=res[::-1]
        l=len(res)
        i=0
        head=newNode(-1)
        prev=head
        while(i<l):
            ptr=newNode(int(res[i]))
            prev.next=ptr
            prev=ptr
            i+=1
        return head.next
