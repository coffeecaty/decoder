# -*- coding: utf-8 -*-
import text

def nminus(x,y):
 m=list(x)
 y=int(y)
 a=0
 Dnm=('0','1','2','3','4','5','6','7','8','9')
 while a<len(m):
  if m[a] in Dnm:
    m[a]=str((y-int(m[a]))%10)
    a=a+1
  else:
   a=a+1 
 z=text.text(m)
 return(z)  

