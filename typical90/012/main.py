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
red = [[False]*w for _ in range(h)]

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

uf = UnionFind(h*w)

q = I()
def union4(y1,x1, y2,x2):
    uf.union(y1*w+x1, y2*w+x2)

for _ in range(q):
    que = LI()
    if que[0] == 1:
        y,x = que[1], que[2]
        y -= 1; x-=1
        red[y][x] = True
        if y>0 and red[y-1][x]:
            union4(y,x,y-1,x)
        if y<h-1 and red[y+1][x]:
            union4(y,x,y+1,x)
        if x>0 and red[y][x-1]:
            union4(y,x,y,x-1)
        if x<w-1 and red[y][x+1]:
            union4(y,x,y,x+1)
    elif que[0] == 2:
        y1,x1,y2,x2 = que[1:]
        y1 -= 1; x1 -= 1
        y2 -= 1; x2 -= 1
        if uf.find(y1*w+x1) == uf.find(y2*w+x2) and red[y1][x1] and red[y2][x2]:
            yes()
        else:
            no()
        


    else:
        assert False, "hogehgoe"
    
