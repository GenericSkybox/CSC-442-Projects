import subprocess
import os

bashCommand = "cd ../.."
bashCommand1 = "touch file1"
bashCommand2 = "ls"

os.system(bashCommand)
os.system(bashCommand1)
os.system(bashCommand2)

"""
Website references
https://stackoverflow.com/questions/4256107/running-bash-commands-in-python - os.system(bashCommand)
https://stackoverflow.com/questions/40608183/how-to-make-a-python-script-to-download-a-file-from-a-ftp-server?rq=1
"""