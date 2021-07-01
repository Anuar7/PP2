class Solution(object):
    def subtractProductAndSum(self, n):
        S, P = 0, 1
        while int(n):
          dig = n % 10
          S += dig
          P *= dig
          n //= 10
        return P - S
        