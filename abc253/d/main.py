#!/usr/bin/env python3
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

n,a,b = LI()

lcm = a * b // math.gcd(a, b)
ans = (n+1)*n//2
ans -= (n-n%a+a)*(n//a)//2
ans -= (n-n%b+b)*(n//b)//2
ans += (n-n%lcm+lcm)*(n//lcm)//2
print(ans)