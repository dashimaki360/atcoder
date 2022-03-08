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

s = S()
k = I()
n = len(s)
sumdot = [0] * (n+1)
for i in range(n):
    if s[i] == '.':
        sumdot[i+1] = sumdot[i] + 1
    else:
        sumdot[i+1] = sumdot[i]

def is_ok(i,x):
    if i+x > n:
        return False
    if sumdot[i+x] - sumdot[i] <= k:
        return True
    else:
        return False


ans = 0
for i in range(n):
    ok = 0
    ng = n + 1
    while ng-ok > 1:
        nxt = (ok+ng)//2
        if is_ok(i,nxt):
            ok = nxt
        else:
            ng = nxt
    ans = max(ans, ok)
print(ans)