#!/usr/bin/env python3
import sys, math
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007

n,q = LI()
Q = [LI() for _ in range(q)]
h = [-1]*(n+1)
b = [-1]*(n+1)

for que in Q:
    t = que[0]
    if t == 1:
        x = que[1]
        y = que[2]
        h[y] = x
        b[x] = y
    elif t == 2:
        x = que[1]
        y = que[2]
        h[y] = -1
        b[x] = -1
    else:
        x = que[1]
        ans = []
        while h[x] != -1:
            x = h[x]
        while b[x] != -1:
            ans.append(x)
            x = b[x]
        ans.append(x)
        ans = [len(ans)] + ans
        print(*ans)
