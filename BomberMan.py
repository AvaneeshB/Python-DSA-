class Solution:
    def solve(self, matrix):
        r={}
        c={}
        count=0
        for i in range(len(matrix)):
            if 1 in matrix[i]:
                for j in range(len(matrix[i])):
                    if matrix[i][j]==1:
                        if i not in r:
                            r.update({i:1})
                        if j not in c:
                            c.update({j:1})
        for i in range(len(matrix)):
            if 0 in matrix[i]:
                for j in range(len(matrix[i])):
                    if matrix[i][j]==0:
                        if (i in r) or (j in c):
                            continue
                        else:
                            count+=1
        return count
