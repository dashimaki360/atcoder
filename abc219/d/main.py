#!/usr/bin/env python3
import sys, math
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007
INF = 1001001001

n = I()
x,y = LI()
AB = [LI() for _ in range(n)]

dp = [[INF]*(y+1) for _ in range(x+1)]
dp[0][0] = 0
for i in range(n):
    a = AB[i][0]; b = AB[i][1]
    for j in range(x, -1, -1):
        for k in range(y, -1, -1):
            j2 = min(x,j+a)
            k2 = min(y,k+b)
            dp[j2][k2] = min(dp[j2][k2], dp[j][k]+1)
ans = dp[x][y]
if ans > n:
    ans = -1
print(ans)
