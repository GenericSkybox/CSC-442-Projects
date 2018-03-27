import os
import ftplib

ftp = ftplib.FTP("jeangourd.com")
ftp.login("anonymous", "")


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
"""