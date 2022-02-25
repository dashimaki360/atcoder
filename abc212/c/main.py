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

n,m = LI()
A = LI()
B = LI()
A.sort()
B.sort()

i = 0
j = 0
ans = 1001001001
while i < n and j < m:
    diff = abs(A[i]- B[j])
    ans = min(ans, diff)
    if A[i] > B[j]:
        j += 1
    else:
        i += 1
print(ans)