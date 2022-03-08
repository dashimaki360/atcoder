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

n,q = LI()
graph = [[] for _ in range(n)]
dists = [-1]*n
for _ in range(n-1):
    a, b = LI()
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)  # 有向グラフなら消す

que = deque()
que.append(0)
dists[0] = 0
while len(que) > 0:
    x = que.popleft()
    # print("X",x)
    for to in graph[x]:
        if dists[to] == -1:
            dists[to] = dists[x] + 1
            que.append(to)


# print(graph)
# print(dists)
for _ in range(q):
    c,d = LI()
    if (dists[c-1] + dists[d-1])%2==0:
        print("Town")
    else:
        print("Road")

