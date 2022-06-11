#!/usr/bin/env python3
import sys, math
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007
from collections import deque

h,w = LI()
S = []
for _ in range(h):
    S.append(input())

ans = -1
delta = [[1,0],[0,1],[-1,0],[0,-1]]

def solve(i,j):
    global ans
    if S[i][j] == "#": return
    dist = [[-1]*w for _ in range(h)]
    que = deque()
    que.append([i,j])
    dist[i][j] = 0
    while len(que):
        x,y = que.popleft()
        d = dist[x][y]
        for dx,dy in delta:
            if x+dx>=h or x+dx < 0: continue
            if y+dy>=w or y+dy < 0: continue
            if S[x+dx][y+dy] == "#": continue
            if dist[x+dx][y+dy] != -1: continue
            dist[x+dx][y+dy] = d+1
            ans = max(ans, d+1)
            que.append([x+dx,y+dy])

for i in range(h):
    for j in range(w):
        solve(i,j)
print(ans)
