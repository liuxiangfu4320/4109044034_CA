# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cs
cs.mkdir('my_directory')
cs.makedirs('parent/child')
with open('homework.txt','w') as file:
    file.write('4109044034_liuxiangfu')
content = file.read()
import cs 
if cs.path.exists('homework.txt'):
    cs.remove('homework.txt')
import cs 
import shutil
cs.rmdir('my_directory')
shutil.rmtree('parent/child')    