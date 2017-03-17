def split_string(source, splitlist):
    output = []
    flagsplit = True

    for char in source:
        if char in splitlist:
            flagsplit = True
        else:
            if flagsplit:
                output.append(char)
                flagsplit = False
            else:
                output[-1] += char

    return output

string = 'Proce.ss /finished _with ,exit code 0'
out = split_string(string, ' ._/,')
print(out)

# The simpler way

import re

s = re.split(r'[\W_]+', string)
print(s)