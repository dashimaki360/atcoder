#!/usr/bin/env python3
import sys, math
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007

def rot(s):
    return list(zip(*s[::-1]))

def find_left_top(s):
    for i in range(n):
        for j in range(n):
            if s[i][j] == '#':
                return i,j

def is_same(s,t):
    si, sj = find_left_top(s)
    ti, tj = find_left_top(t)
    offset_i = ti-si
    offset_j = tj-sj
    for i in range(n):
        for j in range(n):
            ii = i + offset_i
            jj = j + offset_j
            if 0<= ii < n and 0<=jj<n:
                if s[i][j] != t[ii][jj]: return False
            else:
                if s[i][j] == '#': return False
    return True

n = int(input())
s = [input() for _ in range(n)]
t = [input() for _ in range(n)]

cntS = sum(1 for i in range(n) for j in range(n) if s[i][j]=='#')
cntT = sum(1 for i in range(n) for j in range(n) if t[i][j]=='#')
if cntS != cntT:
    no()
    exit()

for _ in range(4):
    if is_same(s,t):
        yes()
        exit()
    s = rot(s)
no()
