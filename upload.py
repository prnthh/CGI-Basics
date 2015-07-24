#!/usr/bin/python
import cgi, cgitb, os, subprocess


########################################################
httpPre = """
<html>
<head><title>Server admin page</title></head>
<body>

<form enctype="multipart/form-data" action="uploaded.py" method="post">
<p>File: <input type="file" name="file">
<p><input type="submit" value="Upload"></p>
</form>


</body>
</html>
"""
########################################################

print ("Content-type: text/html\n\r\n\r")
print httpPre

