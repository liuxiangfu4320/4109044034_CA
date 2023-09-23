# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
os.mkdir('CS')
file_path = os.path.join('CS','homework.txt')
with open(file_path,'w')as file:
    file.write('4112028022_liuxiangfu')
with open(file_path,'r')as file:
    content = file.read()
print("檔案內容:",content)
print("\n檔案資訊:")
print("資訊:",os.path.getsize(file_path),"bytes")
os.remove(file_path)
os.rmdir('CS')