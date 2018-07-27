#!/usr/bin/python
#this program is used to query a DB for 'serial' and return the first matching value as a json object
import sqlite3
import cgi, cgitb
import json

#to return sqlite results as json valid dictionaries
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

form = cgi.FieldStorage()

if form.getvalue('serialno'):
    serial = form.getvalue('serialno')
    conn = sqlite3.connect('userData.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    cur.execute("SELECT * from USERS where SERIALNO=\"" + serial+"\"")
    res = cur.fetchone()
    if(res!=None):print("Set-Cookie: serialno="+serial)
    print("Content-type: application/json\r\n\r\n")
    print json.dumps(res)
    conn.close()
else:
    print("Content-type: text/plain\r\n\r\n")
    print 300



