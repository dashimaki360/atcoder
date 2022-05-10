#!/usr/bin/env python3
import sys, math ,heapq, bisect
from collections import deque
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 998244353
INF = 10**18

n,q = LI()
ans = [0]*n
tb = [0]*n
for i in range(n):
    tb[i] = i 
    ans[i] = i

for _ in range(q):
    x = I()
    x -= 1
    
    idx = tb[x]
    if idx+1 == n:
        sidx = idx-1
    else:
        sidx = idx+1
    r = ans[sidx]

    tmp = ans[idx]
    ans[idx] = ans[sidx]
    ans[sidx] = tmp

    tmp = tb[x]
    tb[x] = tb[r]
    tb[r] = tmp

    # print(*ans)

for i in range(n):
    ans[i] += 1
print(*ans)


