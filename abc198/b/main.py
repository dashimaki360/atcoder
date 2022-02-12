#!/usr/bin/env python3
n = input()

for i in range(11):
    x = "0"*i + n
    if x == x[::-1]:
        print("Yes")
        break
else:
    print("No")

