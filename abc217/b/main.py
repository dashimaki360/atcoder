#!/usr/bin/env python3
cons = ["ABC" , "ARC" , "AGC" , "AHC"]
s1 = input()
s2 = input()
s3 = input()
S = [s1, s2, s3]
for con in cons:
    if not con in S:
        print(con)
        break
