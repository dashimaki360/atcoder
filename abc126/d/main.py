#!/usr/bin/env python3
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")

N = I()

graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b, w = LI()
    graph[a-1].append([b-1,w])
    graph[b-1].append([a-1,w])  # 有向グラフなら消す

import collections
que = collections.deque()
colors = [-1]*N
colors[0] = 0
que.append(0)
while len(que):
    x = que.popleft()
    for to, w in graph[x]:
        if colors[to] != -1: continue
        if w&1:
            colors[to] = colors[x]^1
        else:
            colors[to] = colors[x]
        que.append(to)
for c in colors:
    print(c)