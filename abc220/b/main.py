#!/usr/bin/env python3
k = int(input())
a,b = map(int, input().split())
K = 1 
a10 = 0
b10 = 0
while a > 0 or b > 0:
    a10 += a%10 * K
    b10 += b%10 * K
    a = a//10
    b = b//10
    K *= k
    # print(a10)

print(a10*b10)
