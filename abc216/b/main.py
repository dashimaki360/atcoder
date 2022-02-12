#!/usr/bin/env python3
n = int(input())
L = []
for i in range(n):
    L.append(input())
if len(set(L)) == n:
    print("No")
else:
    print("Yes")

