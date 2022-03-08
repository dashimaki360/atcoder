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
AB = [LI() for _ in range(n)]

x = []
for a,b in AB:
    x.append(a)
    x.append(a+b)

y = sorted(set(x))
d = { v: i for i, v in enumerate(y) }

l = [0]*len(y)
ans = [0]*(n+1)
for a,b in AB:
    l[d[a]] += 1
    l[d[a+b]] -= 1

day = 0
num = 0
for i in range(len(l)):
    dif = y[i] - day
    day = y[i]
    ans[num] += dif
    num += l[i]

print(*ans[1:])
