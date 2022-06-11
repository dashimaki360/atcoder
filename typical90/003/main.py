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

n = I()
graph = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = LI()
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)  # 有向グラフなら消す

def solve(i):
    depth = [-1]*n
    def dfs(x, d):
        depth[x] = d
        for to in graph[x]:
            if depth[to] != -1: continue
            dfs(to, d+1)
    dfs(i, 0)
    maxd = max(depth)
    maxi = depth.index(maxd)
    return maxi, maxd

i,_ = solve(0)
_,ans = solve(i)
print(ans+1)
    
