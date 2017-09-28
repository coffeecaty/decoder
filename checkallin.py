# -*- coding: utf-8 -*-

def checkallin(a,l=[]):
 a =list(str(a))
 n=0
 while n<len(a):
    if a[n] not in  l:
     return False
    else:
        n=n+1
 return True
