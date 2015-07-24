#to execute system shell commands and read the output via STDOUT
import subprocess
process = subprocess.Popen('uptime', stdout=subprocess.PIPE)
out, err = process.communicate()

#for IP address of the client
import os
x = os.environ["REMOTE_ADDR"]


#read or write
log = open("/home/pi/serverFiles/files/log.txt", "rw")
content = log.read()
log.write("content to be written")


#cookies
x = os.environ["HTTP_COOKIE"]
fileList = os.listdir("/home/pi/serverFiles/files/")
