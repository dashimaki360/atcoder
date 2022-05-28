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
s = S()
ans = s.count('R') * s.count('G') * s.count('B')
for i in range(1,n//2+5):
    for j in range(n):
        if j+i+i >= n:
            continue
        if len(set([s[j],s[j+i],s[j+i+i]])) == 3:
            ans -= 1
print(ans)
