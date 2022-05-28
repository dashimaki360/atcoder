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

n,q = LI()
path = [[] for _ in range(n)]
depth = [-1] * n
cnt = [0] * n
for _ in range(n-1):
    a,b = LI()
    a -= 1
    b -= 1
    path[a].append(b)
    path[b].append(a)

for _ in range(q):
    p, x = LI()
    p -= 1
    cnt[p] += x

depth[0] = 0
def dfs(x):
    for p in path[x]:
        if depth[p] != -1:
            continue
        depth[p] = depth[x] + 1
        cnt[p] += cnt[x]
        # print(cnt)
        dfs(p)

dfs(0)
print(*cnt)



