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
INF = 10**18

n,m = LI()
g = [[INF]*n for _ in range(n)]
for _ in range(m):
    a, b, c= LI()
    a-=1; b-=1
    g[a][b] = c

ans = 0
for i in range(n):
    for a in range(n):
        for b in range(n):
            if a==b: continue
            g[a][b] = min(g[a][b], g[a][i]+g[i][b])
            if g[a][b] != INF: ans += g[a][b]
print(ans)

