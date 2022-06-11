#!/usr/bin/env python3
from itertools import permutations
import sys, math
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007

s1 = input()
s2 = input()
s3 = input()
s1 = list(map(ord, list(s1)))
s2 = list(map(ord, list(s2)))
s3 = list(map(ord, list(s3)))

a = set()
a = a.union(s1,s2,s3)
a = list(a)
m = len(a)
inv = [0]*255
for i, _a in enumerate(a):
    inv[_a] = i

if m > 10:
    print("UNSOLVABLE")
    exit()

def charsToS(chars):
    ret = []
    for sx in [s1, s2, s3]:
        tmp = 0
        for i, ss in enumerate(sx[::-1]):
            tmp += chars[inv[ss]]*(10**i)
        ret.append(tmp)
    return ret

def check(chars):
    if chars[inv[s1[0]]] == 0 or chars[inv[s2[0]]] == 0 or chars[inv[s3[0]]] == 0:
        return False
    i1, i2, i3 = charsToS(chars)
    return i1+i2 == i3

def printAns(chars):
    i1, i2, i3 = charsToS(chars)
    print(i1)
    print(i2)
    print(i3)


for seq in permutations(range(10), m):
    if check(seq):
        printAns(seq)
        break
else:
    print("UNSOLVABLE")






