#!/usr/bin/env python3
import sys, math
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007

def dist(a,b,c,d):
    return (a-c)**2 + (b-d)**2

x1,y1,x2,y2 = LI()


for i in range(x1-10, x1+10):
    for j in range(y1-10, y1+10):
        if dist(i,j,x1,y1) == dist(i,j,x2,y2) == 5:
            print("Yes")
            exit()
else:
    print("No")