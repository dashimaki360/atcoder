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

s = S()
q = I()
flip = 0
head = []
tail = []
for i in range(q):
    que = input()
    if que=="1":
        flip = (flip+1)%2
    else:
        if (int(que[2]) + flip)%2 == 1:
            head.append(que[4])
        else:
            tail.append(que[4])
ans = "".join(head)[::-1] + s + "".join(tail)
if flip:
    ans = ans[::-1]
print(ans)

