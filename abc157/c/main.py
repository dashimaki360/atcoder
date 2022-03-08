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

n,m = LI()
A = [LI() for _ in range(m)]

for i in range(2000):
    if len(str(i)) != n:
        continue
    for s,c in A:
        if str(i)[s-1] != str(c):
            break
    else:
        print(i)
        exit()
print(-1)
