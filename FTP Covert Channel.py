import os
from ftplib import FTP

DEBUG = False

ip = "jeangourd.com"
username = "anonymous"
password = ""
folder_path = "/../../mnt/c/Users/eortiz/Desktop/FTP"

file1 = "main.txt"
file2 = "seven.txt"
file3 = "ten.txt"
bin1 = "binary_main.txt"
bin2 = "binary_seven.txt"
bin3 = "binary_ten.txt"

directory_1 = "7"
directory_2 = "10"
filematch = "*.*"
data = []

# START #
# First we're going to change our folder to a directory to store our files we're going to create
print("Welcome to Pride's FTP permission decoder")
os.chdir(folder_path)
print("Folder navigated")
ftp = FTP(ip)
ftp.login(username, password)
print("Login successful")

if DEBUG:
    print("File List:")

ftp.cwd(directory_1)

ftp.dir(data.append)

f = open(file1, "w+")
for _file in data:
    if DEBUG:
        print(_file)

    f.write("%s\r\n" % _file)

print("Permissions saved")
f.close()

"""

ftp.cwd(directory_1)
print("File List:")
ftp.dir(data.append)

f = open(file2, "w+")
for _file in data:
    print(_file)
    f.write("%s\r\n" % _file)

f.close()


ftp.cwd("/")
ftp.cwd(directory_2)
print("File List:")
ftp.dir(data.append)

f = open(file3, "w+")
for _file in data:
    print(_file)
    f.write("%s\r\n" % _file)

f.close()
"""
ftp.quit()
print("FTP Server exited")

permissionarray = []
with open(file1, 'r') as f:
    for line in f:
        if not line[0:3] == "---":
            continue
        else:
            permissionarray.append(line[3:10])

f.close()
print("Storing file permissions only")

os.system("rm %s" % file1)
print("%s cleanup" % file1)

f = open(bin1, "w+")
for i in permissionarray:
    tempbin = ""

    for j in i:
        if j == '-':
            tempbin += '0'
        else:
            tempbin += '1'

    if DEBUG:
        print(tempbin)

    f.write(tempbin)

f.close()
print("Permissions decoded to binary")

os.chdir("../Python/Cyber Storm Assignments")
os.system("python Binary\ Decoder.py < ../../FTP/%s" % bin1)


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