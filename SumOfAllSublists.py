def modu(a):
    return a%(1000000007)

class Solution:
    def solve(self, nums):
        l=len(nums)
        res=0
        for i in range(l):
                res+=nums[i]*(i+1)*(l-i)
        return modu(res)
