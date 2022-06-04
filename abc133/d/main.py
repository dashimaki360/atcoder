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
A = LI()

x = 0
for i in range(n):
    if i&1:
        x -= A[i]
    else:
        x += A[i]
x = x//2
print(2*x)
for i in range(n-1):
    x = A[i]-x
    print(2*x)




