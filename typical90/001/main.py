#!/usr/bin/env python3
from re import X
import sys, math ,heapq, bisect
from collections import deque
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 998244353
INF = 10**18

def main():
    n,l = LI()
    k = I()
    A = LI()
    
    ok = 0
    ng = l + 10
    def is_ok(x):
        last = 0
        cnt = 0
        for a in A:
            if a - last >=x:
                cnt += 1
                last = a
            if cnt >= k and l-last >= x:
                return True
        return False
        
    while (ng-ok) > 1:
        x = (ok+ng)//2
        if is_ok(x):
            ok = x
        else:
            ng = x
    print(ok)


if __name__ == '__main__':
    main()
