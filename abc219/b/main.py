#!/usr/bin/env python3
s = []
s.append(input())
s.append(input())
s.append(input())
A = input()
ans = ""
for a in A:
    ans += s[int(a)-1]
print(ans)

