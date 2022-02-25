#!/usr/bin/env python3
import sys, math
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007

n = I()
A = LI()
B = LI()
ans = 0
for i in range(n):
    if A[i] >= B[i]:
        ans += B[i]
    else:
        ans += A[i]
        x = min(A[i+1], B[i] - A[i])
        ans += x
        A[i+1] -= x
print(ans)

