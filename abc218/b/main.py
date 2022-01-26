#!/usr/bin/env python3
s = list(map(int, input().split()))
ans = []
for ss in s:
    ans.append(chr(ord("a") + ss - 1))
print("".join(ans))

