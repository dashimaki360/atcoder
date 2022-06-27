#!/usr/bin/env python3
import sys, math ,heapq, bisect
from collections import deque
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007
INF = 10**18    

n = I()
X = [0]*n
Y = [0]*n
P = [0]*n
for i in range(n):
    X[i], Y[i], P[i] = map(int, input().split())

def dist(a,b):
    return abs(X[a]-X[b]) + abs(Y[a]- Y[b])

def bfs(st, max_dist):
    visited = [0]*n
    que = deque()
    que.append(st)
    visited[st] = 1
    while len(que):
        x = que.popleft()
        for i in range(n):
            if x == i or visited[i]: continue
            if dist(x,i) > P[x] * max_dist: continue
            que.append(i)
            visited[i] = 1
    return 0 not in visited

def is_ok(max_dist):
    for i in range(n):
        if bfs(i, max_dist):
            return True
    return False

def is_ok2(max_dist):
    d = [[1]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if dist(i,j) <= P[i] * max_dist:
                d[i][j] = 0 
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
    for i in range(n):
        if 1 not in d[i]:
            return True
    return False

ok = 10**10
ng = 0
while ok-ng > 1:
    x = (ok+ng)//2
    # if is_ok(x):
    if is_ok2(x):
        ok = x
    else:
        ng = x
print(ok)
