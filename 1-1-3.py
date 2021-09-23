# task3
import re

ind = False
print("Enter your expression")
try:
    el = input("")
    if el.isdigit():
        print(el, 'correct')
        ind = True
    regexp = re.compile(r'[^+-0-9\s]')
    if ind is False:
        if len(regexp.findall(el)):
            print(eval(el), 'correct')
        else:
            print('False, None')
except:
    if ind is False:
        print("False, None")
