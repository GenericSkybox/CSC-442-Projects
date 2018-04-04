###################################################################
# Name:  Team Pride: Eric Ortiz, Colby Austin, Andy Kraus, Herbert Sanford, Jalen Senones, Stephen Kunz, Tony York
# Date:  4/6/18
# Class: CSC 442 - 001
# Desc:  This program logs into Dr. Gourd's FTP server, grabs his file permissions, translates it to binary, and then
#        uses our existing Binary Decoder to decode the message. The message is printed to the console while the actual
#        binary is saved to a file on our system.
####################################################################

import ftplib
from ftplib import FTP

DEBUG = False

# Initialize the ip address, username, and password for the FTP server
ip = "jeangourd.com"
username = "anonymous"
password = ""

# Initialize a 2-D list of directories, where the first row indicates the path of the directory on the FTP server and
# the second row defines what the bit-type of that directory is (or at least what it's expected to be)
list_of_directories = [["/", "/7", "/10"], [7, 7, 10]]
list_of_strings = []


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


# This function converts a string of permissions into binary, then sends that binary to another function to be
# translated
def convert(file_string, bintag):
    # We'll start by creating a blank string to add all of our binary to later
    binary = ""

    # Now we'll iterate through the file string passed in. If the permission is blank (i.e. -), then we add a 0 to the
    # binary string. Otherwise, we'll add a 1
    for char in file_string:
        if char == "-":
            binary += "0"
        else:
            binary += "1"

    # If the bit-type is 10, then we need to strip any excess 0's off the end of the binary string
    if bintag == 10:
        # Create a temp variable
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

    # Now here is where we copy-paste our Binary Decoder from earlier
    # Grab the data from the binary string, strip it of unnecessary characters (just in case), and determine the length
    # of the binary number left
    data = binary
    data = data.replace('\r\n', '')
    data = data.replace('\r', '')
    data = data.replace('\n', '')
    data = data.replace(' ', '')
    datalen = len(data)

    if DEBUG:
        print(data)
        print(datalen)

    # If the data string is divisible by only 7, then the binary is 7-bit, and we will translate appropriately
    if datalen % 7 == 0:
        if DEBUG:
            print("Binary string is 7-bit")

        translate(data, 7)

    # Otherwise, something went wrong and the binary number wasn't properly stripped
    else:
        if DEBUG:
            print(data)

        print("Error: binary string is not 7-bit")
        exit()


# This function is used to grab a list of files from a given directory on the FTP and return the the file permissions as
# a string
def grab(directory, bintag):
    # Before we start, let's reset the data array just in case...
    data = []
    # We should probably reset what directory we're in before we move to a different one...
    ftp.cwd("/")
    # We're also gonna set up a blank string so that we can easily add file permissions to it later and return it
    file_string = ""

    # Then we navigate to the directory from which we wanna grab the list of files from, and then we add it to data list
    ftp.cwd(directory)
    ftp.dir(data.append)

    if DEBUG:
        print("File List:")

    # So now we're going to iterate through each line in the list of files in the server
    for _file in data:
        if DEBUG:
            print(_file)

        # For each line, we're going to add only the file permissions to the file string
        if bintag == 7:
            # If it's a bit-type of 7, then we ignore any files that start with d, r, or w, and save the last 7 file
            # permissions otherwise
            if not _file[0:3] == "---":
                continue
            else:
                file_string += _file[3:10]
        else:
            # Else, the bit-type is ten, so we'll save the whole permission snippet
            file_string += _file[0:10]

    if DEBUG:
        print(file_string)

    return file_string


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

# Now we're going to iterate through the list of directories and grab the file permissions from each directory. We'll
# append these to our list of strings
for i in range(len(list_of_directories[0])):
    list_of_strings.append(grab(list_of_directories[0][i], list_of_directories[1][i]))

# Then we nope out of the FTP server since we have all of the file permissions
ftp.quit()
print("FTP Server exited")

# Lastly, we'll iterate through our list of strings to convert them to binary - this also depends on the the bit-type of
# the directory we originally grabbed the string from
for i in range(len(list_of_strings)):
    convert(list_of_strings[i], list_of_directories[1][i])

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