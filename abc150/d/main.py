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

n,m = LI()
A = list(set(LI()))
A = list(map(lambda x: x//2, A))

l = 1
for a in A:
    l = l*a//math.gcd(l,a)
for a in A:
    if (l//a)%2 == 0:
        print(0)
        exit()

ans = m//l 
ans = (ans+1)//2
print(ans)


