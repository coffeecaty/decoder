# -*- coding: utf-8 -*-
from printf import printf
from AToa import AToa
from tkinter import Tk
NUMN=('0','1','2','3','4','5','6','7','8','9')
NUME=('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25')
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
 elif way == 'shift':
   import shift
   decode = shift.shift(code)
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
 elif way == 'rot':
   while 1 :
    foot=input('请输入位移的步长(0-25,默认13):')
    if foot in NUME:
        break
    elif foot == '':
        foot = 13
        break
    else:
        print('请输入合法的步长')
   import rot
   decode = rot.rot(code,foot)
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
 elif way == 'nplus':
   while 1 :
    foot=input('请输入位移的步长(0-9，默认1):')
    if foot in NUMN:
        break
    elif foot == '':
        foot = 1
        break
    else:
        print('请输入合法的步长')
   import nplus
   decode = nplus.nplus(code,foot)
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
 elif way == 'nminus':
   while 1 :
    foot=input('请输入位移的步长(0-9，默认9):')
    if foot in NUMN:
        break
    elif foot == '':
        foot = 9
        break
    else:
        print('请输入合法的步长')
   import nminus
   decode = nminus.nminus(code,foot)
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

