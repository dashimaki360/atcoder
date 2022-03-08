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

n,d = LI()
A = [LI() for _ in range(n)]

A.sort(key=lambda x:x[1])
ans = 0
i = 0
while i < n:
    x = A[i][1] + d -1
    ans += 1
    while x >= A[i][0]:
        i += 1
        if i >= n: break

print(ans)
