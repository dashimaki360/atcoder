#!/usr/bin/env python3
import sys, math
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")

k = int(input())
s = input()
t = input()

def C(l):
  point = 0
  for i in [1,2,3,4,5,6,7,8,9]:
    cnt = 0
    for ll in l:
      if i == ll:
        cnt += 1
    point += i*(10**cnt)
  return point

def win(ta,ao):
  return C(ta) > C(ao)
  
def p(ta,ao):
  x = k
  y = k
  for i in range(4):
    if ta[i] == ta[4]:
      x -= 1
    if ao[i] == ta[4]:
      x -= 1
    if ao[i] == ao[4]:
      y -= 1
    if ta[i] == ao[4]:
      y -= 1
  if ta[4] == ao[4]:
    y -= 1
  if x < 0 or y < 0:
    return 0
  return x*y

ta = [0]*5
ao = [0]*5
for i in range(4):
  ta[i] = int(s[i])
  ao[i] = int(t[i])
ans = 0
for i in [1,2,3,4,5,6,7,8,9]:
  for j in [1,2,3,4,5,6,7,8,9]:
    ta[4] = i
    ao[4] = j
    if win(ta,ao):
      pp = p(ta,ao)
      ans += pp
print(ans/(k*9-8)/(k*9-9))