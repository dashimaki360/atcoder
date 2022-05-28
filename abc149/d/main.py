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

n, k = LI()
r,s,p = LI()
t = S()
T = [0]*n
P = [0]*n
for i in range(n):
    if t[i] == 'r':
        T[i] = 'r'
        P[i] = p
    elif t[i] == 's':
        T[i] = 's'
        P[i] = r
    elif t[i] == 'p':
        T[i] = 'p'
        P[i] = s

ans = 0
for i in range(n):
    if i-k >=0 and T[i] == T[i-k]:
        T[i] = 'x'
    else:
        ans += P[i]
print(ans)



