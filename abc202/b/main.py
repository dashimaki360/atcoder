#!/usr/bin/env python3
s = input()
s2 = s[::-1]
s3 = []
for i in range(len(s2)):
    if s2[i] == '6':
        s3.append('9')
    elif s2[i] == '9':
        s3.append('6')
    else:
        s3.append(s2[i])
print(''.join(s3))