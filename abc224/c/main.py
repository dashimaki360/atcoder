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
A = [LI() for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if (A[i][0]-A[j][0])*(A[i][1]-A[k][1]) != (A[i][0]-A[k][0])*(A[i][1]-A[j][1]):
                ans += 1
print(ans)
