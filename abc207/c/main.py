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
qs = []
for i in range(n):
    t,l,r = LI()
    if t == 1:
        qs.append([l*2,r*2])
    elif t == 2:
        qs.append([l*2,r*2-1])
    elif t == 3:
        qs.append([l*2+1,r*2])
    elif t == 4:
        qs.append([l*2+1,r*2-1])
ans = 0
for i in range(n):
    for j in range(i+1,n):
        if qs[i][1] < qs[j][0] or qs[j][1] < qs[i][0]:
            continue
        else:
            ans += 1
print(ans)
