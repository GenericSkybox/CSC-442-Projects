###################################################################
# Name:  Eric Ortiz
# Date:  3/28/18
# Class: CSC 442 - 001
# Desc:  This program decodes binary into both 7-bit and 8-bit ASCII
####################################################################

# library used for reading standard input
import sys

# grab the data from the file and determine the length of the binary number
data = sys.stdin.read()
datalen = len(data)

# DEBUG: print the data we just collected and its length
"""
print(data)
print(datalen)
"""

# in case we need the binary later, store the data into a temporary variable
tempdata = data
# define a list of characters that will later be concatenated together to form a sentence
charlist = []

# if the length of the data is a multiple of 7 AND 8, then we cannot determine which bit-type of ASCII its written in
# therefore, we'll just print both and have the user read it to determine
if datalen % 8 == 0 and datalen % 7 == 0:
    print("binary string can be either 7-bit or 8-bit")

    # although there's better ways to do it, we just need a loop that continues until the data string is empty
    while True:
        # we grab the first 8 characters of the data string and convert that binary bit into an integer
        bchar = tempdata[:8]
        bint = int(bchar, 2)
        # then we convert the integer into a character and append it to our list of characters
        character = chr(bint)
        charlist.append(character)

        # DEBUG:
        # print(character)

        # if there's more than 8 characters left in the data string, "cut off" the first 8 characters of it and store it
        if (len(tempdata) > 8):
            tempdata = tempdata[8:]
        # else, we've gone through the entire string
        else:
            break

    # we concatenate all of our characters into one string and print that
    finalstring = ''.join(charlist)
    print(finalstring)

    # since we don't know whether or not the characters are 7-bit or 8-bit, we'll do the same thing again, but for 7-bit
    while True:
        bchar = tempdata[:7]
        bint = int(bchar, 2)
        character = chr(bint)
        charlist.append(character)

        # DEBUG:
        # print(character)

        if (len(tempdata) > 7):
            tempdata = tempdata[7:]
        else:
            break

# if the data string is divisible by only 8, then the characters are 8-bit ASCII
elif datalen % 8 == 0:
    print("binary string is 8-bit")

    while True:
        bchar = tempdata[:8]
        bint = int(bchar, 2)
        character = chr(bint)
        charlist.append(character)

        # DEBUG:
        # print(character)

        if (len(tempdata) > 8):
            tempdata = tempdata[8:]
        else:
            break

# if the data string is divisible by only 7, then the characters are 7-bit ASCII
elif datalen % 7 == 0:
    print("binary string is 7-bit")

    while True:
        bchar = tempdata[:7]
        bint = int(bchar, 2)
        character = chr(bint)
        charlist.append(character)

        # DEBUG:
        # print(character)

        if (len(tempdata) > 7):
            tempdata = tempdata[7:]
        else:
            break

# otherwise, the string is a combination of both
else:
    print("binary string is a combination of 7-bit and 8-bit")
    print("Error: multi-bit binary detected")

# lastly, we concatenate all of our characters into one string and print that
finalstring = ''.join(charlist)
print(finalstring)

"""
First the program needs to read from standard input a string of binary
Then we need to determine whether or not the binary is 7-bit, 8-bit, or both
Regardless of the bit type, we need to translate each group of digits into characters
Re-concatenate the characters into a string and print it
"""