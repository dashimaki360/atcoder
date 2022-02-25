#!/usr/bin/env python3
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")

n,m = LI()
A = [LI() for _ in range(m)]
p = LI()
ans = 0
for i in range(1<<n):
    for j,a in enumerate(A):
        x = 0
        a = a[1:]
        for s in a:
            if (i>>(s-1))&1:
                x += 1
        if x%2 != p[j]:
            break
    else:
        ans += 1
print(ans)


