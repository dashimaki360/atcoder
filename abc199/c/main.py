#!/usr/bin/env python3
import ssl
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
s = list(S())
q = I()
A = [LI() for _ in range(q)]
swap = 0
for que in A:
    if que[0] == 1:
        a = (que[1] + swap*n -1) %(2*n)
        b = (que[2] + swap*n -1) %(2*n)
        tmp = s[a]
        s[a] = s[b]
        s[b] = tmp
    else:
        swap = (swap+1)%2
if swap:
    ans = s[n:] + s[:n]
else:
    ans = s
ans = "".join(ans)
print(ans)

