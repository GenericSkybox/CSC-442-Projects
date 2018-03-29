# import os for system commands on our system and ftplib for actually accessing the FTP server
import os
from ftplib import FTP

# Debug mode initialized to false
DEBUG = False

# Initialize the ip address, username, and password for the FTP server
ip = "jeangourd.com"
username = "anonymous"
password = ""
# Also initialize where we want to store the binary (on our system) once we grab it from the server
folder_path = "/../../mnt/c/Users/erico/Desktop/FTP"

# Here are some file names that we'll use to distinguish between all of the folders we're sifting through on the server
# File1-3 is for initially storing the permissions, while bin1-3 is for the actual binary
file1 = "main.txt"
file2 = "seven.txt"
file3 = "ten.txt"
bin1 = "binary_main.txt"
bin2 = "binary_seven.txt"
bin3 = "binary_ten.txt"

# These are the directory names on the FTP server where we need to grab the file permissions
directory_1 = "/"
directory_2 = "7"
directory_3 = "10"

# Lastly, we declare an array of data, which is where we'll initially store the file permissions from each directory...
data = []
# ... and an array of permissions which we'll grab from each line from a list of files
permissions = []

# This function is used to grab a list of files from a given directory on the FTP and save it to a file on your system
def grab(filename, directory):
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

    # Now that we have the list of files, we're going to add each string representation of the file we grabbed to a text
    # file on our system

    # To do this, we're going to write to a new (or existing) file on our system each file in our data array
    f = open(filename, "w+")

    for _file in data:
        # If we're in debug, print each file as we save it
        if DEBUG:
            print(_file)

        # Also, we can't just add each file string straight up. We need to add some line endings to the end
        f.write("%s\r\n" % _file)

    # Then we close the file
    print("List of files saved")
    f.close()

# This function grabs the list of files that we have saved and stores just the file permissions based on the bintag
# Once they're stored, we'll go ahead and convert them to binary and save it to binary name file
def storeAndConvert(filename, binname, bintag):
    # Before we start, let's reset the permission array just in case...
    permissions = []
    # Let's re-open the file where we stored the list of files from the FTP server, but this time we read each line
    with open(filename, 'r') as f:
        # So we read each line from the file...
        for line in f:
            # ... and if the binary tag is 7, then we ignore files that start don't start with --- in the permissions
            if bintag == 7:
                if not line[0:3] == "---":
                    continue
                else:
                    # Also we save just the permissions we care about
                    permissions.append(line[3:10])
            # Otherwise, go ahead and add the whole permission line
            else:
                permissions.append(line[0:10])

    # Once we're done storing permissions to the permission array, go ahead and close the file we were working in
    f.close()
    print("Storing file permissions only")

    # Go ahead and delete that file since we won't need it anymore
    os.system("rm %s" % filename)
    print("%s cleanup" % filename)

    # Now we're going to open up a new file to store our binary in
    f = open(binname, "w+")
    for i in permissions:
        # We set up a temporary binary string, which we'll add to and eventually write to the file
        tempbin = ""

        # For every character in each line, we check to see if it's a - or a letter
        for j in i:
            if j == '-':
                # If it's a dash, then the binary is 0
                tempbin += '0'
            else:
                # Otherwise, it's a 1
                tempbin += '1'

        # Once we're done with each line, we can print out the binary string
        if DEBUG:
            print(tempbin)

        # Lastly, we write the binary string to the file
        f.write(tempbin)

    # If the binary tag is 10, we need to trim off some extra binary bits off of the end of our binary string
    if bintag == 10:
        # Close the file we were working on and then re-open it as a read only (there's probably an easier way to do
        # this)
        f.close()
        with open(binname, 'r') as f:
            # We set the oldbinary number to the one line in the text file
            oldbinary = f.readline()

            if DEBUG:
                print("Before cut: %i" % len(oldbinary))

            # Then we set up how much we're gonna strip off of the end of the old binary - the binary string needs to be
            # a multiple of 7
            bincutoff = len(oldbinary) - (len(oldbinary) % 7)

            if DEBUG:
                print("Cut off: %i" % bincutoff)

            # Now we create the new binary string using the old binary string and the cutoff position
            newbinary = oldbinary[:bincutoff]

            if DEBUG:
                print("After cut: %i" % len(newbinary))

        # Now we close the file and re-open it again, but this time we're writing to the file (again, there's probably
        # an easier way to do this). Then we write the newbinary string to the file, which will overwrite the old one
        f.close()
        f = open(binname, "w+")
        f.write(newbinary)

    # Now that we're done, close the file
    f.close()
    print("Permissions decoded to binary")

# START #
print("Welcome to Pride's FTP permission decoder")
# First we're going to change our folder to a directory to store our files we're going to create
os.chdir(folder_path)
print("Folder navigated")
# Now we're going to login to the FTP server, using the ip, username, and password previously initialized
ftp = FTP(ip)
ftp.login(username, password)
print("Login successful")

# Now we actually grab the string representation of the list of files from the FTP server. We do this by passing in
# where we want to store the list of files and what directory we're grabbing this list from
grab(file1, directory_1)
grab(file2, directory_2)
grab(file3, directory_3)

# Then we nope out of the FTP server since we have all that we need
ftp.quit()
print("FTP Server exited")

# Now that we have the list of files, let's store the permissions and then convert them to binary
# To do that, we pass in the file we're reading from, the binary text file we're making, and the binary tag
storeAndConvert(file1, bin1, 7)
storeAndConvert(file2, bin2, 7)
storeAndConvert(file3, bin3, 10)

# Lastly, we're going to move back to where the Binary Decoder is stored and run it on our three binary text files
os.chdir("../My Programs/Python/Cyber Storm Projects")
os.system("python Binary\ Decoder.py < ../../../FTP/%s" % bin1)
os.system("python Binary\ Decoder.py < ../../../FTP/%s" % bin2)
os.system("python Binary\ Decoder.py < ../../../FTP/%s" % bin3)

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
"""