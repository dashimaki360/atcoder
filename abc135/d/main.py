#!/usr/bin/env python3
import sys, math
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007

s = input()
dp = [[0]*13 for _ in range(len(s)+1)]
dp[0][0] = 1

def update(i, x):
    x = x*pow(10, i, 13)
    x %= 13
    for j in range(13):
        dp[i+1][(x+j)%13] += dp[i][j] %MOD

for i,c in enumerate(s[::-1]):
    if c == "?":
        for x in range(10):
            update(i,x)
    else:
        x = int(c)
        update(i,x)
ans = dp[len(s)][5] %MOD
print(ans)

