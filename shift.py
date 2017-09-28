# -*- coding: utf-8 -*-
import text

def shift(x):
 y=list(x)
 Dshift={'!':'1','@':'2','#':'3','$':'4','%':'5','^':'6','&':'7','*':'8','(':'9',')':'0'}
 n=0
 while n < len(y):
     
   if y[n] in Dshift:
       y[n]=Dshift[y[n]]
       n=n+1
   else:
       n=n+1
 z=text.text(y)
 return(z)
