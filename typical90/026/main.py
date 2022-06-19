#!/usr/bin/env python3
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
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

color = [-1]*n
def dfs(x, bw):
    color[x] = bw
    for to in graph[x]:
        if color[to] != -1: continue
        dfs(to, bw^1)

dfs(0,0)

# print(color)

black = color.count(1)
white = n-black
if black > white:
    choice = 1
else:
    choice = 0
ans = []
for i, c in enumerate(color):
    if c == choice:
        ans.append(i+1)
print(*ans[:n//2])


    

