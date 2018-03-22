###################################################################
# Name:  Eric Ortiz
# Date:  3/28/18
# Class: CSC 442 - 001
# Desc:  This program encodes and decodes strings using a Vinegere Cipher and a key
####################################################################

# import the library for reading the command line and creating enums
import sys
from enum import Enum

# here we create the enums for all the options for our program
class Option(Enum):
    ENCODE = 0
    DECODE = 1


# this method reads the arguments from the command line before the program is really executed
def read():
    # the first argument should be the option, while the second one is the key
    option = sys.argv[1]
    key = sys.argv[2]

    # if the option is -e, then we encode messages
    if option == "-e":
        flag = Option.ENCODE
    # if it's -d, then we decode messages
    elif option == "-d":
        flag = Option.DECODE
    # else, we error
    else:
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
            print("Goodbye")
            exit()
        # if we're reading the input from a file, then we ignore the new line character
        elif '\n' in message:
            message = message[:len(message)-1]

        print(message)

        # if we were told to encode, then execute encode using the key
        if flag == Option.ENCODE:
            print("Encoding!")
            encode(key, message)
        # if we were told to decode, then execute decode using the key
        elif flag == Option.DECODE:
            print("Decoding!")
            decode(key, message)
        else:
            print("Error: This shouldn't happen - the flag is wrong.")
            exit()

# this method actually encodes the message using the key originally passed in
def encode(key, message):
    pass

# this method actually decodes the message using the key originally passed in
def decode(key, message):
    pass


# START #
# if we're given more or less than 3 arguments, then error; otherwise, interpret the arguments via read()
if len(sys.argv) == 3:
    read()
else:
    print("Error: Incorrect number of arguments.")
    exit()