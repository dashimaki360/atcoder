#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
mi = s
ma = s
for i in range(len(s)):
    s2 = s[i:] + s[:i]
    mi = min(mi,s2)
    ma = max(ma,s2)
print(mi)
print(ma)
    
