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
A = LI()
B = LI()
C = LI()

bl = [0]*100101
cl = [0]*100101
for c in C:
    cl[c] += 1
for i,b in enumerate(B):
    bl[b] += cl[i+1]

ans = 0
for a in A:
    ans += bl[a]
print(ans)


