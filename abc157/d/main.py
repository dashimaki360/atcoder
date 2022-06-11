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

n,m,k = LI()
uf = UnionFind(n)

cnt = [0]*n
for i in range(m):
    a,b = LI()
    a -= 1
    b -= 1
    uf.union(a,b)
    cnt[a] += 1
    cnt[b] += 1


for i in range(k):
    c,d = LI()
    c -= 1
    d -= 1
    if uf.find(c) == uf.find(d):
        cnt[c] += 1
        cnt[d] += 1

ans = [0]*n
for i in range(n):
    ans[i] = max(0, uf.size(i) - 1 - cnt[i])

print(*ans)