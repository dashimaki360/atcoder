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

n,m = LI()
path = [[] for _ in range(n)]
for _ in range(m):
    a,b = LI()
    a -= 1
    b -= 1
    path[a].append(b)
    path[b].append(a)

def solve(i,d):
    dist = dict()
    dist[i] = 0
    que = deque()
    que.append(i)
    ret = 0
    while len(que):
        x = que.popleft()
        ret += x+1
        if dist[x] == d: continue
        for p in path[x]:
            if p in dist.keys(): continue
            dist[p] = dist[x] + 1
            que.append(p)
    return ret

q = I()
for _ in range(q):
    x,k = LI()
    print(solve(x-1,k))


