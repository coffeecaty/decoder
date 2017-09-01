# -*- coding: utf-8 -*-
import text

def rot(x,y):
 m=list(x)
 y=int(y)
 a=0
 Drot=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
 while a<len(m):
  if m[a] in Drot:
    b=Drot.index(m[a])
    m[a]=Drot[(b+y)%len(Drot)]
    a=a+1
  else:
   a=a+1 
 z=text.text(m)
 return(z)  
