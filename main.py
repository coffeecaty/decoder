# -*- coding: utf-8 -*-
from printf import printf
from AToa import AToa
from tkinter import Tk
code = AToa(Tk().clipboard_get())
code_origin = code
import help
help.help()
while 1:
 way = AToa(input('解密方法'))
 if way == 'reversed' :
   import reversed
   decode = reversed.reversed_my(code)
   printf(decode)
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
 elif way == 'atbash':
   import atbash
   decode = atbash.atbash(code)
   printf(decode)
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
 elif way == 'quit':
  break
 elif way == 'resetcode':
  code = code_origin
  print('code已重置为',code,'请重新选择解码方式')
 elif way == 'help':
  help.help()
 else:
   print('请选择正确的解码姿势')

