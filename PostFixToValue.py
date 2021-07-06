# Example 1
# Input
# exp = ["9", "3", "+", "2", "/"]
# Output
# 6
# Explanation
# (9 + 3) / 2 = 6



OPERATIONS = {"+": add, "-": sub, "*": mul, "/": lambda a, b: int(a / b)}

class Solution:
    def solve(self, exp):
        stack = []

        for x in exp:
            if x in OPERATIONS:
                b, a = stack.pop(), stack.pop()
                stack.append(OPERATIONS[x](a, b))
            else:
                stack.append(int(x))

        return stack[-1]
