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

s = input()
o = s.count('o')
x = s.count('x')
q = s.count('?')

ans = 0
for i in range(10000):
    t = "0000" + str(i)
    t = t[-4:]
    ng = 0
    for j in range(o):
        if str(j) not in t:
            ng = 1
            break
    if ng: continue
    for j in range(x):
        if str(9-j) in t:
            ng = 1
            break
    if ng: continue
    ans += 1

print(ans)



