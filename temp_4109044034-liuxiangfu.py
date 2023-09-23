# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
os.mkdir('my_life')
os.makedirs('home/house')
with open('homework.txt','w') as file:
    file.write('4109044034_liuxiangfu')
content = file.read()
import os 
if os.path.exists('homework.txt'):
    os.remove('homework.txt')
import os 
import shutil
os.rmdir('my_life')
shutil.rmtree('home/house')    