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

dp = [0]*n
def dfs(pos, pre):
    dp[pos] = 1
    for to in graph[pos]:
        if to == pre: continue
        dfs(to, pos)
        dp[pos] += dp[to]

dfs(0,-1)
ans = 0
for d in dp:
    ans += (n-d)*d
print(ans)