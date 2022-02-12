#!/usr/bin/env python3
n = int(input())
a_name = ""
a_hight = -1
b_name = ""
b_hight = -2
for _ in range(n):
    s, x = input().split()
    x = int(x)
    if x > a_hight:
        b_name = a_name
        b_hight = a_hight
        a_name = s
        a_hight = x
    elif x > b_hight:
        b_name = s
        b_hight = x
    
print(b_name)