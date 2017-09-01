# -*- coding: utf-8 -*-
from AToa import AToa
decode=0
code=0
while 1:
   update = AToa(input('对结果解码请按y,对原码重解请按n,退出请按其他任意键:'))
   if update == 'y':
      code = decode
      print('密码更新为',code,'请继续选择解码方式')
   elif update == 'n':
      print('密码扔为',code,'请重新选择解码方式') 
   else :
      over=AToa(input('确认退出请输入q:'))
      if over == 'q':
        break
      else:
        print('密码扔为',code,'请重新选择解码方式')
