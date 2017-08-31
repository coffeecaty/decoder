# -*- coding: utf-8 -*-

import win32clipboard as wc
import win32con

def paste():
    wc.OpenClipboard()
    copy_text = wc.GetClipboardData(win32con.CF_TEXT)
    wc.CloseClipboard()
    return copy_text

print(paste())
