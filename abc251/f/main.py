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
for i in range(m):
    u,v = LI()
    u -= 1
    v -= 1
    path[u].append(v)
    path[v].append(u)


visited = [0]*n
ans = []
def dfs(x):
    global ans
    for p in path[x]:
        if not visited[p]:
            visited[p] = 1
            print(x+1, p+1)
            dfs(p)
visited[0] = 1
dfs(0)

visited = [0]*n
visited[0] = 1
q = deque()
q.append(0)
while len(q) > 0:
    now = q.pop()
    for p in path[now]:
        if not visited[p]:
            visited[p] = 1
            print(now+1, p+1)
            q.append(p)
