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

h,w = LI()
rs, cs = LI()
rt, ct = LI()
rs -= 1; cs -= 1
rt -= 1; ct -= 1
s = [input() for _ in range(h)]

def solve():
    vecs = [[1,0],[0,1],[-1,0],[0,-1]]
    dp = [[[INF]*4 for _ in range(w)] for _ in range(h)]
    que = deque()
    for i in range(4):
        que.append([rs,cs,i])
        dp[rs][cs][i] = 0
    while len(que):
        y,x,v = que.popleft()
        cost = dp[y][x][v]
        for nv in range(4):
            if cost + 1 < dp[y][x][nv]:
                dp[y][x][nv] = cost+1
                que.append([y,x,nv])
        yy = y+vecs[v][0]
        xx = x+vecs[v][1]
        if yy == rt and xx == ct:
            return dp[y][x][v]
        if yy < 0 or h <= yy or xx < 0 or w <= xx: continue
        if s[yy][xx] == "#": continue
        if cost < dp[yy][xx][v]:
            que.appendleft([yy,xx,v])
            dp[yy][xx][v] = cost

import heapq
def solve_dije():
    vecs = [[1,0],[0,1],[-1,0],[0,-1]]
    dp = [[[INF]*4 for _ in range(w)] for _ in range(h)]
    que = []
    for i in range(4):
        heapq.heappush(que, [0, rs, cs, i])
        dp[rs][cs][i] = 0

    while len(que):
        _, y,x,v = heapq.heappop(que)
        cost = dp[y][x][v]
        for nv in range(4):
            if cost + 1 < dp[y][x][nv]:
                dp[y][x][nv] = cost+1
                heapq.heappush(que, [cost+1, y, x, nv])
        yy = y+vecs[v][0]
        xx = x+vecs[v][1]
        if yy == rt and xx == ct:
            return dp[y][x][v]
        if yy < 0 or h <= yy or xx < 0 or w <= xx: continue
        if s[yy][xx] == "#": continue
        if cost < dp[yy][xx][v]:
            heapq.heappush(que, [cost, yy, xx, v])
            dp[yy][xx][v] = cost

# ans = solve()
ans = solve_dije()
print(ans)

