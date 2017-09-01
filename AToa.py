# -*- coding: utf-8 -*-
import text

def AToa(x):
 y=list(x)
 DAToa={'A':'a','B':'b','C':'c','D':'d','E':'e','F':'f','G':'g','H':'h','I':'i','J':'j','K':'k','L':'l','M':'m','N':'n','O':'o','P':'p','Q':'q','R':'r','S':'s','T':'t','U':'u','V':'v','W':'w','X':'x','Y':'y','Z':'z'}
 n=0
 while n < len(y):
     
   if y[n] in DAToa:
       y[n]=DAToa[y[n]]
       n=n+1
   else:
       n=n+1
 z=text.text(y)
 return(z)
