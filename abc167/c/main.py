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

n,m,x = LI()
A = [LI() for _ in range(n)]
ans = math.inf
for i in range(1<<n):
    yen = 0
    l = [0]*m
    for j in range(n):
        if i>>j&1 == 0:
            continue
        yen += A[j][0]
        for k in range(m):
            l[k] += A[j][k+1]
    if min(l) >= x:
        ans = min(ans, yen)
if ans == math.inf:
    ans = -1
print(ans)


