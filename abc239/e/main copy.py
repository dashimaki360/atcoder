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

n,q = LI()
X = LI()
AB = [LI() for _ in range(n-1)]
VK = [LI() for _ in range(q)]
memo = [False]*n
x_list = [[X[i]] for i in range(n)]
tree = [[] for _ in range(n)]

for a, b in AB:
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)
# print(tree)

def set_x_list(n):
    global x_list
    memo[n] = True
    for t in tree[n]:
        if memo[t]:
            continue
        x_list[n].extend(set_x_list(t))
        x_list[n] = x_list[n][:20]
    return x_list[n]

set_x_list(0)
for i in range(n):
    x_list[i].sort(reverse=True)
for v, k in VK:
    print(x_list[v-1][k-1])





