#!/usr/bin/env python3
from ctypes import Union
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

n = I()
P = LI()
Q = LI()
uf = UnionFind(n)
for p,q in zip(P,Q):
    uf.union(p-1,q-1)

fibo = [0]*(n+5)
fibo[0] = 1
fibo[1] = 3
for i in range(n+1):
    fibo[i+2] = (fibo[i] + fibo[i+1])%MOD

ans = 1
d = defaultdict(int)
for i in range(n):
    x = uf.find(i)
    d[x] += 1
for x in d.values():
    # print(x, fibo[x-1])
    ans *= fibo[x-1]
    ans %= MOD
print(ans)


