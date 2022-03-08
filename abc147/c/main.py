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
A = [[] for _ in range(n)]
for a in A:
    k = I()
    for i in range(k):
        a.append(LI())

ans = -1
for i in range(1<<n):
    tmp = 0
    ng = 0
    for j in range(n):
        if i>>j&1 == 0:
            continue
        else:
            tmp += 1
        for x,y in A[j]:
            if i>>(x-1)&1 != y:
                ng = 1
                break
    if ng == 0:
        ans = max(ans, tmp)
print(ans)


