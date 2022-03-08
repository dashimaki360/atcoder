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




n = I()
root = [[] for _ in range(n)]
memo = [False] * n

def dfs(x):
    memo[x] = True
    print(x+1)
    for r in root[x]:
        if memo[r]:
            continue
        dfs(r)
        print(x+1)



for i in range(n-1):
    a,b = LI()
    a -= 1
    b -= 1
    root[a].append(b)
    root[b].append(a)

for i in range(n):
    root[i].sort()

dfs(0)