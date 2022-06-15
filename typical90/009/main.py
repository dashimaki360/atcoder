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

n = I()
points = []
for _ in range(n):
    x,y = LI()
    points.append([x,y])

def solve(b):
    # sort
    bx = points[b][0]
    by = points[b][1]
    t = []
    for i in range(n):
        if i == b: continue
        x = points[i][0] - bx
        y = points[i][1] - by
        tmp = math.degrees(math.atan2(y,x))
        t.append(tmp)
    t.sort()

    # serch all a
    ret = 0.0
    for i in range(len(t)):
        target = t[i] + 180.0
        if target > 360.0: target -= 360.0
        pos1 = bisect.bisect_left(t, target)

        cand_idx1 = pos1 % len(t)
        cand_idx2 = (pos1 - 1) % len(t)
        candidate1 = min(abs(t[cand_idx1] - t[i]), 360-abs(t[cand_idx1] - t[i]))
        candidate2 = min(abs(t[cand_idx2] - t[i]), 360-abs(t[cand_idx2] - t[i]))
        ret = max(ret, candidate1, candidate2)
    return ret

ans = 0
for b in range(n):
    ret = solve(b)
    ans = max(ans, ret)
print(ans)