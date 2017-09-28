# -*- coding: utf-8 -*-


def polybuis(x):
 from checkallin import checkallin
 Dcheck=('1','2','3','4','5')
 y=list(x)
 if len(y)%2==0 and checkallin(x,Dcheck):
  Dpolybuis=[['a','b','c','d','e'],['f','g','h','i/j','k'],['l','m','n','o','p'],['q','r','s','t','u'],['v','w','x','y','z']]
  n=0
  z=[]
  while n<len(y):
         z.append(y[n:n+2])
         n=n+2
  m=0
  while m<len(z):
      z[m]=Dpolybuis[int(z[m][0])-1][int(z[m][1])-1]
      m=m+1
  import text
  z=text.text(z)
 else:
  print('此code无法进行polybuis操作，请尝试其他解码方法')
  z=x




     

 
 return(z)

print(polybuis(input()))
