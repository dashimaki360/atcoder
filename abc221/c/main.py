#!/usr/bin/env python3
import sys, math
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007

n = S()
x = list(n)
ans = 0
for i in range(1<<(len(x))):
    a = []
    b = []
    for j in range(len(x)):
        if i >> j &1:
            a.append(x[j])
        else:
            b.append(x[j])
    if a == [] or b == []:
        continue
    a.sort(reverse=True)
    a = int(''.join(a))
    b.sort(reverse=True)
    b = int(''.join(b))
    ans = max(ans, a*b)
print(ans)

