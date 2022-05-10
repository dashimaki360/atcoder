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
MOD = 1000000007
INF = 10**18

Q = I()
que = []
p = 0
for i in range(Q):
    q = LI()
    if q[0] == 1:
        que.append([q[1], q[2]])
    elif q[0] == 2:
        c = q[1]
        num = 0
        su = 0
        while 1:
            num += que[p][1]
            if num < c:
                su += que[p][0] * que[p][1]
                p += 1
            else:
                su += que[p][0] *(que[p][1]-num+c)
                que[p][1] = num-c
                break
        print(su)