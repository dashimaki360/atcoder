#!/usr/bin/env python3
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")

h,w = LI()
s = [S() for _ in range(h)]

row = [[0]*w for _ in range(h)]
col = [[0]*w for _ in range(h)]

for i in range(h):
    tmp = 0
    for j in range(w):
        if s[i][j] == "#":
            tmp = 0
        else:
            tmp += 1
            row[i][j] = tmp
    ma = 0
    for j in reversed(range(w)):
        if s[i][j] == "#":
            ma = 0
        else:
            ma = max(row[i][j], ma)
            row[i][j] = ma

for j in range(w):
    tmp = 0
    for i in range(h):
        if s[i][j] == "#":
            tmp = 0
        else:
            tmp += 1
            col[i][j] = tmp
    ma = 0
    for i in reversed(range(h)):
        if s[i][j] == "#":
            ma = 0
        else:
            ma = max(col[i][j], ma)
            col[i][j] = ma

ans = -1
for i in range(h):
    for j in range(w):
        ans = max(ans, row[i][j]+col[i][j] -1)
print(ans)
