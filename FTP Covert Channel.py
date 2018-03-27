import os
from ftplib import FTP

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

os.chdir(folder_path)
ftp = FTP(ip)
ftp.login(username, password)


print("File List:")
ftp.dir(data.append)

f = open(file1, "w+")
for _file in data:
    print(_file)
    f.write("%s\r\n" % _file)

f.close()


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

ftp.quit()



"""
bashCommand = "cd ../.."
bashCommand1 = "touch file1"
bashCommand2 = "ls"
bashCommand3 = "rm file1"

os.system(bashCommand)
os.system(bashCommand1)
os.system(bashCommand2)
os.system(bashCommand3)
"""

"""
Website references
https://stackoverflow.com/questions/4256107/running-bash-commands-in-python - os.system(bashCommand)
https://stackoverflow.com/questions/25793015/change-permissions-via-ftp-in-python
https://stackoverflow.com/questions/21194691/retrieve-file-s-from-ftp-using-python-connection
https://askubuntu.com/questions/528411/how-do-you-view-file-permissions
https://docs.python.org/3/library/ftplib.html
https://www.guru99.com/reading-and-writing-files-in-python.html
https://stackoverflow.com/questions/111954/using-pythons-ftplib-to-get-a-directory-listing-portably
"""