###################################################################
# Name:  Team Pride: Eric Ortiz, Colby Austin, Andy Kraus, Herbert Sanford, Jalen Senones, Stephen Kunz, Tony York
# Date:  4/6/18
# Class: CSC 442 - 001
# Desc:  This program logs into Dr. Gourd's FTP server, grabs his file permissions, translates it to binary, and then
#        uses our existing Binary Decoder to decode the message. The message is printed to the console while the actual
#        binary is saved to a file on our system.
####################################################################

# import os for system commands on our system and ftplib for actually accessing the FTP server
import os
import ftplib
from ftplib import FTP

DEBUG = False

# Initialize the ip address, username, and password for the FTP server
ip = "jeangourd.com"
username = "anonymous"
password = ""

# These are the directory names on the FTP server where we need to grab the file permissions
directory_1 = "/"
directory_2 = "/7"
directory_3 = "/10"

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

# This function is used to grab a list of files from a given directory on the FTP and save it to a file on your system
def grab(directory, bintag):
    # Before we start, let's reset the data array just in case...
    data = []
    # We should probably reset what directory we're in before we move to a different one...
    ftp.cwd("/")

    # Then we navigate to the directory from which we wanna grab the list of files from, and then we add it to data list
    ftp.cwd(directory)
    ftp.dir(data.append)

    # If we're in debug, show that we're about to print the list of files
    if DEBUG:
        print("File List:")

    # NEW
    file_string = ""

    for _file in data:
        # If we're in debug, print each file as we save it
        if DEBUG:
            print(_file)

        # NEW
        if bintag == 7:
            if not _file[0:3] == "---":
                continue
            else:
                file_string += _file[3:10]
        else:
            file_string += _file[0:10]

    if DEBUG:
        print(file_string)

    return file_string

def convert(file_string, bintag):
    binary = ""

    for char in file_string:
        if char == "-":
            binary += "0"
        else:
            binary += "1"

    if bintag == 10:
        # Close the file we were working on and then re-open it as a read only (there's probably an easier way to do
        # this)
        # We set the oldbinary number to the one line in the text file
        oldbinary = binary

        if DEBUG:
            print("Before cut: %i" % len(oldbinary))

        # Then we set up how much we're gonna strip off of the end of the old binary - the binary string needs to be
        # a multiple of 7
        bincutoff = len(oldbinary) - (len(oldbinary) % 7)

        if DEBUG:
            print("Cut off: %i" % bincutoff)

        # Now we create the new binary string using the old binary string and the cutoff position
        binary = oldbinary[:bincutoff]

        if DEBUG:
            print("After cut: %i" % len(binary))

    if DEBUG:
        print(binary)

    data = binary

    data = data.replace('\r\n', '')
    data = data.replace('\r', '')
    data = data.replace('\n', '')
    data = data.replace(' ', '')
    datalen = len(data)

    if DEBUG:
        print(data)
        print(datalen)

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

# START #
print("Welcome to Pride's FTP permission decoder")
# First, we're going to login to the FTP server, using the ip, username, and password previously initialized
try:
    ftp = FTP(ip)
    ftp.login(username, password)
    print("Login successful")
except ftplib.all_errors as e:
    print(e)
    exit()

# Now we actually grab the string representation of the list of files from the FTP server. We do this by passing in
# where we want to store the list of files and what directory we're grabbing this list from
list1 = grab(directory_1, 7)
list2 = grab(directory_2, 7)
list3 = grab(directory_3, 10)

# Then we nope out of the FTP server since we have all that we need
ftp.quit()
print("FTP Server exited")

convert(list1, 7)
convert(list2, 7)
convert(list3, 10)

"""
Website references
https://stackoverflow.com/questions/4256107/running-bash-commands-in-python - os.system(bashCommand)
https://stackoverflow.com/questions/25793015/change-permissions-via-ftp-in-python
https://stackoverflow.com/questions/21194691/retrieve-file-s-from-ftp-using-python-connection
https://askubuntu.com/questions/528411/how-do-you-view-file-permissions
https://docs.python.org/3/library/ftplib.html
https://www.guru99.com/reading-and-writing-files-in-python.html
https://stackoverflow.com/questions/111954/using-pythons-ftplib-to-get-a-directory-listing-portably
https://stackoverflow.com/questions/3277503/how-do-i-read-a-file-line-by-line-into-a-list
https://stackoverflow.com/questions/3169725/python-error-catching-ftp
"""