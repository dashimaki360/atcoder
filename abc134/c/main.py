#!/usr/bin/env python3
import sys, math
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007

n = I()
A = [int(input()) for _ in range(n)]
x = sorted(A)
max1 = x[-1]
max2 = x[-2]
for a in A:
    if a == max1:
        print(max2)
    else:
        print(max1)
