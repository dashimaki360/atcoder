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
x = I()

suma = sum(A)
k = x//suma
sum = suma*k
ans = len(A)*k
for a in A:
    sum += a
    ans += 1
    if sum > x:
        break
print(ans)

