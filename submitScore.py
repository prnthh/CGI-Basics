#!/usr/bin/python
#accept parameters and insert into sqlite table
import sqlite3
import cgi, cgitb
import json
import datetime
form = cgi.FieldStorage()

if form.getvalue('serialno'):
    serial = form.getvalue('serialno')
    gname = form.getvalue('gname')
    score = form.getvalue('score')

    conn = sqlite3.connect('userData.db', isolation_level=None) #commits query immediately
    cur = conn.cursor()
    stri = "INSERT INTO SCORES VALUES(?,?,?,?)"
    cur.execute(stri, (serial, gname, score, datetime.datetime.now()))
    print("Content-type: text/plain\r\n\r\n")
    print 200
    conn.close()
else:
    print("Content-type: text/plain\r\n\r\n")
    print 300



