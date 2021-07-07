# You are given a two-dimensional list of integers intervals where each list represents an inclusive [start, end] interval.

# Return the total unique duration it covers.
# Example:-
# Input
# intervals = [
#     [45, 60],
#     [1, 5],
#     [5, 15],
#     [2, 3]
# ]
# Output
# 31
# Explanation
# The total unique covered distance is [45, 60] (duration of 16) and [1 ,15] (duration of 15).


def chk(li,b):
    if li[1]<=b[1]:
        return [True,b]
    elif li[0]<=b[1]:
        return [True,[b[0],li[1]]]
    else:
        return [False,b,li]
class Solution:
    def solve(self, intervals):
        intervals.sort()
        res=[]
        for i in range(len(intervals)):
            if i==0:
                res.append(intervals[i])
            else:
                ind=chk(intervals[i],res.pop())
                if ind[0]:
                    res.append(ind[1])
                    
                else:
                    res.append(ind[1])
                    res.append(ind[2])
        ans=0
        for i in res:
            ans+=i[1]-i[0]+1
        return ans
