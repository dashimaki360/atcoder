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
from collections import Counter

n,k = LI()
C = LI()
cnt = Counter(C[:k])
ans = len(cnt)

for i in range(n):
    if i+k >= n:
        break
    cnt[C[i]]-=1
    cnt[C[i+k]]+=1
    if cnt[C[i]] == 0:
        del cnt[C[i]]
    ans = max(ans, len(cnt))
print(ans)
    

