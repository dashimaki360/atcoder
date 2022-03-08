#!/usr/bin/env python3
import collections
import sys, math
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007
import heapq


que = []
heapq.heapify(que)
offset = 0

def one(x):
    heapq.heappush(que, x-offset)

def two(x):
    global offset
    offset += x

def three():
    a = heapq.heappop(que)
    a += offset
    print(a)

q = I()
for i in range(q):
    s = input()
    if s == "3":
        three()
    else:
        t, x = map(int, s.split())
        if t==1:
            one(x)
        elif t==2:
            two(x)
