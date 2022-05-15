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

from collections import defaultdict
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

n,m = LI()
path = [[] for _ in range(n)]
for i in range(m):
    u,v = LI()
    u -= 1
    v -= 1
    path[u].append(v)
    path[v].append(u)


uf = UnionFind(n)
ans = []
def dfs(x):
    global ans
    for p in path[x]:
        if uf.find(x) != uf.find(p):
            uf.union(x, p)
            print(x+1, p+1)
            dfs(p)
dfs(0)

uf = UnionFind(n)
q = deque()
q.append(0)
while len(q) > 0:
    now = q.pop()
    for p in path[now]:
        if uf.find(now) != uf.find(p):
            uf.union(now, p)
            print(now+1, p+1)
            q.append(p)
