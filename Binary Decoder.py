###################################################################
# Name:  Eric Ortiz
# Date:  3/28/18
# Class: CSC 442 - 001
# Desc:  This program decodes binary into both 7-bit and 8-bit ASCII
####################################################################

# Library used for reading standard input
import sys

DEBUG = False

# This function converts a string of binary (i.e. "tempdata") into an actual string, depending on the bit-type of the
# binary (i.e. "n")
def translate(tempdata, n):
    # First define a list of characters that will later be concatenated together to form a sentence
    charlist = []

    # Although there's better ways to do it, we just need a loop that continues until the data string is empty
    while True:
        # We grab the first n (bit-type) characters of the data string, convert that binary bit into an integer, then
        # convert that integer into a character
        bchar = tempdata[:n]
        bint = int(bchar, 2)
        character = chr(bint)

        # If the character is a backspace, then truncate the list by 1
        if character == '\b':
            charlist = charlist[:-1]
        # Otherwise, append it to our list of characters
        else:
            charlist.append(character)

        if DEBUG:
            print(character)

        # If there's more than n (bit-type) characters left in the data string, we "cut off" the first n characters of
        # the string and store the rest
        if (len(tempdata) > n):
            tempdata = tempdata[n:]
        # Else, we've gone through the entire string
        else:
            break

    # Once we have our character list, we concatenate all of our characters into one string and print it
    finalstring = ''.join(charlist)
    print(finalstring)


# START #
# Grab the data from the file, strip it of unnecessary characters, and determine the length of the binary number left
data = sys.stdin.read()
data = data.replace('\r\n', '')
data = data.replace('\r', '')
data = data.replace('\n', '')
data = data.replace(' ', '')
datalen = len(data)

if DEBUG:
    print(data)
    print(datalen)

# If we don't have any binary numbers to convert, error and exit
if data == "":
    print("Error: Binary string empty.")
    exit()

# If the length of the data is a multiple of 7 AND 8, then we cannot determine which bit-type of ASCII its written in.
# Therefore, we'll just print both and have the user read it to determine the message themselves
if datalen % 8 == 0 and datalen % 7 == 0:
    if DEBUG:
        print("Binary string can be either 7-bit or 8-bit")

    # Since we don't know if the binary is 7-bit or 8-bit, we'll call translate twice with different bit-types
    translate(data, 8)
    translate(data, 7)

# If the data string is divisible by only 8, then the binary is 8-bit, and we will translate appropriately
elif datalen % 8 == 0:
    if DEBUG:
        print("Binary string is 8-bit")

    translate(data, 8)

# If the data string is divisible by only 7, then the binary is 7-bit, and we will translate appropriately
elif datalen % 7 == 0:
    if DEBUG:
        print("Binary string is 7-bit")

    translate(data, 7)

# Otherwise, the string is a combination of both... so error
else:
    if DEBUG:
        print("Binary string is a combination of 7-bit and 8-bit")

    print("Error: multi-bit binary detected")
    exit()