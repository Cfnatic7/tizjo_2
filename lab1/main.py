#!/usr/bin/env python3

import sys

def reverse_capital_letters(param):
	retval = ''
	for idx in range(0, len(param)):
		if param[idx].isupper():
			retval += param[idx].lower()
		elif param[idx].islower():
			retval += param[idx].upper()
		else:
			retval += param[idx]
	return retval

def my_printf(format_string,param):
    shouldDo=True
    for idx in range(0,len(format_string)):
        if shouldDo and len(format_string) > (idx + 1):
            if format_string[idx] == '#' and format_string[idx+1] == 'k':
                print(reverse_capital_letters(param),end="")
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            shouldDo=True

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
