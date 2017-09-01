# -*- coding: utf-8 -*-
import text

def nplus(x,y):
 m=list(x)
 y=int(y)
 a=0
 Dnp=('0','1','2','3','4','5','6','7','8','9')
 while a<len(m):
  if m[a] in Dnp:
    m[a]=str((int(m[a])+y)%10)
    a=a+1
  else:
   a=a+1 
 z=text.text(m)
 return(z)
