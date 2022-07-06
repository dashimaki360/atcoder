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
c = []
for _ in range(h):
    c.append(input())

reach = [[False]*w for _ in range(h)]
delta = ((-1,0), (1,0), (0,-1), (0,1))

def dfs(x, y, step, st_x, st_y):
    if reach[y][x] and x==st_x and y == st_y:
        return step
    if reach[y][x]:
        return -1000
    reach[y][x] = True
    ret = -1000
    for dx, dy in delta:
        nx = x+dx
        ny = y+dy
        if nx < 0 or nx >= w or ny < 0 or ny >= h: continue
        if c[ny][nx] == "#": continue
        ret = max(ret, dfs(nx, ny, step+1, st_x, st_y))
    reach[y][x] = False
    return ret

def clear():
    for i in range(h):
        for j in range(w):
            reach[i][j] = False

ans = -1000
for y in range(h):
    for x in range(w):
        if c[y][x] == "#": continue
        clear()
        ans = max(ans, dfs(x,y,0,x,y))
if ans < 3:
    ans = -1
print(ans)
