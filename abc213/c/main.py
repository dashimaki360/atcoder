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

h,w,n = LI()
A = []
B = []
for i in range(n):
    a,b = LI()
    A.append(a)
    B.append(b)

# もとの座標をキーに、値に圧縮後の座標を。sorted(list(set(L))) で重複を消して順番に並べる
Adict = {x:i+1 for i,x in enumerate(sorted(list(set(A))))}
Bdict = {y:i+1 for i,y in enumerate(sorted(list(set(B))))}

for i in range(n):
  print(Adict[A[i]], Bdict[B[i]])
