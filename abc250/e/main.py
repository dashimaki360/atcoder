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

def hs():
    L = [0]
    S = set()
    A = [int(a) for a in input().split()]
    s = 0
    for i, a in enumerate(A):
        if a not in S:
            S.add(a)
            s = s ^ ((a * (a + 1346) * (a + 9185)) % P)
        L.append(s)
    return L
P = 8128812800000059
N = int(input())
X, Y = hs(), hs()
Q = int(input())
for _ in range(Q):
    x, y = map(int, input().split())
    print("Yes" if X[x] == Y[y] else "No")