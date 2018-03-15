###################################################################
# Name:  Eric Ortiz
# Date:  3/28/18
# Class: CSC 442 - 001
# Desc:  This program decodes both binary into 7-bit and 8-bit ASCII
####################################################################

import sys

data = sys.stdin.read()
datalen = len(data)

print(data)
print(datalen)

tempdata = data
charlist = []

if datalen % 8 == 0 and datalen % 7 == 0:
    print("binary string can be either 7-bit or 8-bit")

elif datalen % 8 == 0:
    print("binary string is 8-bit")

    while True:
        bchar = tempdata[:8]
        bint = int(bchar, 2)
        character = chr(bint)
        charlist.append(character)
        #print(character)

        if (len(tempdata) > 8):
            tempdata = tempdata[8:]
        else:
            break

elif datalen % 7 == 0:
    print("binary string is 7-bit")

    while True:
        bchar = tempdata[:7]
        bint = int(bchar, 2)
        character = chr(bint)
        charlist.append(character)
        #print(character)

        if (len(tempdata) > 7):
            tempdata = tempdata[7:]
        else:
            break

else:
    print("binary string is a combination of 7-bit and 8-bit")

finalstring = ''.join(charlist)
print(finalstring)

"""
First the program needs to read from standard input a string of binary
Then we need to determine whether or not the binary is 7-bit, 8-bit, or both(?)
Regardless of the bit type, we need to translate each group of digits into characters
Reconcatenate the characters into a string 
"""