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
from collections import deque
INF = 10**18

n,m = LI()
root = [[] for _ in range(n)]
for i in range(m):
    a,b = LI()
    a -=1; b-=1
    root[a].append(b)
    root[b].append(a)

graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = LI()
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)  # 有向グラフなら消す

dist = [INF] * n
cnt = [0] * n
dist[0] = 0
cnt[0] = 1
q = deque()
q.append(0)
while len(q) > 0:
    x = q.popleft()
    for y in root[x]:
        if dist[y] > dist[x]+1:
            dist[y] = dist[x]+1
            q.append(y)
        if dist[y] == dist[x]+1:
            cnt[y] += cnt[x]
ans = cnt[n-1]%MOD
# print(dist,cnt)
print(ans)


