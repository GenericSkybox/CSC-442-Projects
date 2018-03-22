###################################################################
# Name:  Eric Ortiz
# Date:  3/28/18
# Class: CSC 442 - 001
# Desc:  This program encodes and decodes strings using a Vinegere Cipher and a key
####################################################################

# import the library for reading the command line
import sys
#from enum import Enum
from string import whitespace

# enumerating has been taken out since not all version of python come with it pre-packaged
"""
# here we create the enums for all the options for our program
class Option(Enum):
    ENCODE = 0
    DECODE = 1
"""

# this method reads the arguments from the command line before the program is really executed
def read():
    # the first argument should be the option, while the second one is the key
    option = sys.argv[1]
    key = sys.argv[2]

    # if the option is -e, then we encode messages
    if option == "-e":
        flag = 0
    # if it's -d, then we decode messages
    elif option == "-d":
        flag = 1
    # else, we error
    else:
        flag = -1
        print("Error: Incorrect option given.")
        exit()

    # now we can properly execute the program using the key and the option flag
    execute(flag, key)

# this method continually asks the user to submit messages to be encoded or decoded using the key passed in
def execute(flag, key):
    while True:
        # we first grab the message from the command line
        message = sys.stdin.readline()

        # if the user hit Ctrl+D, then we exit instead
        if not message:
            # print("Goodbye")
            exit()
        # if we're reading the input from a file, then we ignore the new line character
        elif '\n' in message:
            message = message[:len(message)-1]

        # DEBUG: print the message to make sure it's what we need it to be
        # print(message)

        # eliminate all whitespace characters from the key
        key = key.translate(None, whitespace)

        # DEBUG: print the key to make sure it's also correct
        # print(key)

        code(key, message, flag)

# this method actually encodes or decodes (based on the flag) the message using the key originally passed in
def code(key, message, flag):
    # initialize the final string we return and the index of the key
    final_string = ""
    key_i = 0

    # we'll iterate through the message and encode/decode it character-by-character
    for i in range(0, len(message)):
        # we need to set flags as to whether the character is a symbol or a flag
        flag_sym = False
        flag_cap = False


        # if the character is lowercase, then we convert it to an integer based off of the ascii table
        if 'a' <= message[i] <= 'z':
            plaintext_ascii_int = ord(message[i]) - 97
        # since uppercase and lowercase are in two different places in the ascii table, we need to subtract by a
        # different value
        elif 'A' <= message[i] <= 'Z':
            plaintext_ascii_int = ord(message[i]) - 65
            flag_cap = True
        # if it's neither uppercase nor lowercase, then we don't need to zero it out
        else:
            plaintext_ascii_int = ord(message[i])
            flag_sym = True


        # we need to convert the key's characters to integers too
        if 'a' <= key[key_i] <= 'z':
            key_ascii_int = ord(key[key_i]) - 97
        elif 'A' <= key[key_i] <= 'Z':
            key_ascii_int = ord(key[key_i]) - 65
        else:
            print("Error: Key contains %s, which is neither a whitespace nor alphabetical character" % key[key_i])
            exit()

        # since the key length doesn't match the message length, we use a different iterator for it
        # if the key iterator goes beyond the length of the key, we reset it to zero
        if key_i >= len(key) - 1:
            key_i = 0
        else:
            key_i += 1


        # if the message character is a symbol, we'll just add it back to the final_string and undo the key iteration
        if flag_sym:
            final_string += chr(plaintext_ascii_int)

            key_i -= 1
            if key_i == -1:
                key_i = len(key) - 1
        # if the message character is capitalized and we're encoding
        elif flag_cap and flag == 0:
            final_string += chr(((plaintext_ascii_int + key_ascii_int) % 26) + 65)
        # if the message character is capitalized and we're decoding
        elif flag_cap and flag == 1:
            final_string += chr(((26 + plaintext_ascii_int - key_ascii_int) % 26) + 65)
        # if the message character is lowercase and we're encoding
        elif flag == 0:
            final_string += chr(((plaintext_ascii_int + key_ascii_int) % 26) + 97)
        # if the message character is lowercase and we're decoding
        elif flag == 1:
            final_string += chr(((26 + plaintext_ascii_int - key_ascii_int) % 26) + 97)
        # else ???? what went wrong?
        else:
            print("Error: This shouldn't happen - somehow the wrong flag was passed in")

    # lastly, we print out the encoded/decoded string
    print(final_string)

# START #
# if we're given at least 3 arguments, interpret the arguments via read(); otherwise, error
if len(sys.argv) >= 3:
    read()
else:
    print("Error: Incorrect number of arguments.")
    exit()