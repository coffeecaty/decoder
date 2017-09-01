# -*- coding: utf-8 -*-
import text

def atbash(x):
 y=list(x)
 Datbash={'a':'z','b':'y','c':'x','d':'w','e':'v','f':'u','g':'t','h':'s','i':'r','j':'q','k':'p','l':'o','m':'n','n':'m','o':'l','p':'k','q':'j','r':'i','s':'h','t':'g','u':'f','v':'e','w':'d','x':'c','y':'b','z':'a'}
 n=0
 while n < len(y):
     
   if y[n] in Datbash:
       y[n]=Datbash[y[n]]
       n=n+1
   else:
       n=n+1
 z=text.text(y)
 return(z)
