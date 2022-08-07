#!/usr/bin/env python3
import sys, math ,heapq, bisect
from collections import deque
from termios import VT1
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


amb = "Ambiguous"
n = I()
q = I()

uf = UnionFind(n)
que0 = []
que1 = []

for _ in range(q):
    t,x,y,v = LI()
    x -= 1
    y -= 1
    if t == 0:
        uf.union(x,y)
        que0.append([x,v])
    else:
        if uf.find(x) != uf.find(y):
            que1.append(amb)
        else:
            que1.append([x,y,v])

A = [0]*n
que0.sort()
for x,v in que0:
    A[x+1] = v - A[x]

for que in que1:
    if que == amb:
        print(amb)
    else:
        x,y,v = que
        if (x - y) & 1 == 0:
            ans = A[y] + v - A[x]
        else:
            ans = A[y] + A[x] - v
        print(ans)

