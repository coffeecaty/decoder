# -*- coding: utf-8 -*-
while 1:
    a=input('input the passcode:')
    l = len(a)
    if l>3:
        break
    else:
        print('the passcode is too short')
b=[]
for n in list(range(1,int(l/2))):
    if l%(int(n)+1)==0:
     b.append(int(n)+1)
for x in b:
	m=0
	print( 'grad',x,'x',int(l/x))
	while m<l:
		print(' '.join(list(a)[m:m+x]))
		m=m+x
