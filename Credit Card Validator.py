# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 14:01:18 2020

@author: Gurpreet
"""

# 2223 1299 6973 0708

import sys

try:
	inputNumber = sys.argv[1]
except:
	inputNumber = '2223 1299 6973 0708'

number = inputNumber.split()
l = [x for x in number[3]]
number.pop()
last = l.pop()
ss = ''.join(l)
number.append(ss)
s = ''.join(number)
rs = s[::-1]
ll = [x for x in rs]

k = []

for i in range(0, 15):
	if i%2==0:
		if int(ll[i])*2 > 9:
			k.append(ll[i].replace(ll[i], str((int(ll[i])*2)-9)))
		else:
			k.append(ll[i].replace(ll[i], str(int(ll[i])*2)))
	else:
		k.append(ll[i])

total = 0

for i in k:
	total += int(k.pop())

if last == total%10:
	print('CARD VALID')
else:
#	Visa: Visa credit card numbers always start with 4.
#
#	MasterCard: MasterCard credit card numbers always start with 51 or 55.
#
#	Discover: Discover credit card numbers always start with 644, 6011 or 605.
#
#	American Express card: American Express credit card numbers always start with 34 or 37.
	
	if inputNumber.startswith('4'):
		print('CARD VALID (VISA)')
	elif inputNumber.startswith('51') or inputNumber.startswith('55'):
		print('CARD VALID (MASTER CARD)')
	elif inputNumber.startswith('644') or inputNumber.startswith('6011') or inputNumber.startswith('605'):
		print('CARD VALID (DISCOVER CARD)')
	elif inputNumber.startswith('34') or inputNumber.startswith('37'):
		print('CARD VALID (AMERICAN EXPRESS CARD)')
	else:
		print('CARD NOT VALID')

input()