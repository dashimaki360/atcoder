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

import itertools

n,k,p = LI()
A = LI()
if n&1:
    A.append(INF+10)
    n += 1

list1 = [[] for _ in range(n//2+1)]
list2 = [[] for _ in range(n//2+1)]

for i in range(1<<(n//2)):
    cnt = 0
    value1 = 0
    value2 = 0
    for j in range(n//2):
        if i>>j&1:
            cnt += 1
            value1 += A[j]
            value2 += A[j+n//2]
    list1[cnt].append(value1)
    list2[cnt].append(value2)

for i in range(n//2+1):
    list1[i].sort()
    list2[i].sort()

ans = 0
for i in range(n//2+1):
    if k-i > n//2 or k-i < 0: continue
    for v1 in list1[i]:
        x = bisect.bisect_right(list2[k-i], p-v1)
        ans += x
print(ans)
