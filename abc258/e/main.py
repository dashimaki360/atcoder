#!/usr/bin/env python3
import sys, math ,heapq, bisect
from collections import deque
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007
INF = 10**18

n,q,x = LI()
W = LI()
sumw = sum(W)
base_num = n * (x//sumw)
W = W+W

def pre_calc():
    to = [-1]*n
    nums = [-1]*n
    r = 0
    weight = 0
    for l in range(n):
        while weight < x%sumw:
            weight += W[r]
            r += 1
        to[l] = r%n
        nums[l] = base_num + r - l
        if l == r:
            r += 1
        else:
            weight -= W[l]

    def calc_G():
        G = [0]
        reached = [False]*n
        reached[0] = True
        while 1:
            next = to[G[-1]]
            if reached[next]:
                break
            G.append(next)
            reached[next] = True
        return G

    return to, nums, calc_G()

to, nums, G = pre_calc()
loop_st = G.index(to[G[-1]])
loop_len = len(G) - loop_st

def solve(k):
    if k <= len(G):
        print(nums[G[k]])
    else:
        loop = (k - len(G))%loop_len
        print(nums[G[loop_st+loop]])

for _ in range(q):
    k = int(input()) - 1
    solve(k)
