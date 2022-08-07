#!/usr/bin/env python3
import sys, math ,heapq, bisect
from collections import deque
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007
INF = 10**18

n,m = LI()
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = LI()
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)  # 有向グラフなら消す

ans = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if j in graph[i] and k in graph[j] and i in graph[k]:
                ans += 1
print(ans)
            
