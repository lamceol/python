
import re

r = stdout[0]
s = 'here are_some words'
t = 'zlxidnvlwienf;lWKDFJ'
# print (re.split(r'(s*)', s))

# print (re.split(r'[_]', r))

# print (re.findall(r'TC[_]', r))

reg = re.findall(r'TC\d{5}', r)

print reg 