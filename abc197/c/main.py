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

n = I()
A = LI()

ans = 1001001001001
for i in range(1 << (n-1)):
    x = []
    for j,a in enumerate(A):
        if j == 0:
            x.append(a)
        elif i >> (j-1) & 1:
            x.append(a)
        else:
            x[-1] |= a
    tmp = 0
    for xx in x:
        tmp ^= xx
    ans = min(ans, tmp)
print(ans)


