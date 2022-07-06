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

n,k = LI()
N = 10**5

def jump(x):
    tmp = x
    while 1:
        tmp += x%10
        x //= 10
        if x == 0:
            return tmp%N

to = [[-1]*64 for _ in range(N)]
for i in range(N):
    to[i][0] = jump(i)

for j in range(1,64):
    for i in range(N):
        to[i][j] = to[to[i][j-1]][j-1]
    
ans = n
for j in range(64):
    if (k>>j) & 1:
        ans = to[ans][j]
print(ans)


