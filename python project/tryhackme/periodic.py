# !/usr/bin/env python 

import periodictable 

# print(vars(periodictable)['H'].number)
with open('element.txt','r') as e:
    elements = e.read();
    elements= elements.splitlines();
# # print(elements2)
hidden = ""
for item in elements:
    # print(f"{item} - {vars(periodictable)[item].number}")
    hidden += chr(vars(periodictable)[item].number)

print(f"Hidden file : {hidden}")