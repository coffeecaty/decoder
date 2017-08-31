#coding=utf-8

import os
def copy(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

