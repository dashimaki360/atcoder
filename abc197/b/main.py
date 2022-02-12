#!/usr/bin/env python3
h,w,x,y = map(int, input().split())
x -= 1
y -= 1
a = []
for _ in range(h):
    a.append(input())

ans = 1  #x,y 

i = 1
while 1:
    if x-i < 0 or a[x-i][y] == "#":
        break
    else:
        ans += 1
    i += 1

i = 1
while 1:
    if x+i >= h or a[x+i][y] == "#":
        break
    else:
        ans += 1
    i += 1

i = 1
while 1:
    if y-i < 0 or a[x][y-i] == "#":
        break
    else:
        ans += 1
    i += 1

i = 1
while 1:
    if y+i >= w or a[x][y+i] == "#":
        break
    else:
        ans += 1
    i += 1
print(ans)