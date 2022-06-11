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

h,w,a,b = LI()

used = [[False]*w for _ in range(h)]
ans = 0

def next(x,y):
    if x != w-1:
        nx = x+1
        ny = y
    else:
        nx = 0
        ny = y+1
    return nx, ny


def dfs(x, y, a_num):
    global ans
    if x == w-1 and y == h-1:
        if a_num == a:
            ans += 1
        return
    nx, ny = next(x,y)
    # hanjo
    dfs(nx,ny,a_num)
    # yoko
    if x != w-1:
        if (not used[y][x]) and (not used[y][x+1]):
            used[y][x] = used[y][x+1] = True
            dfs(nx,ny,a_num+1)
            used[y][x] = used[y][x+1] = False
    # tate
    if y != h-1:
        if (not used[y][x]) and (not used[y+1][x]):
            used[y][x] = used[y+1][x] = True
            dfs(nx,ny,a_num+1)
            used[y][x] = used[y+1][x] = False

dfs(0,0,0)
print(ans)