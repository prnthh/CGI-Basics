#!/usr/bin/python
#to read meta.json for each subdirectory and return a json directory listing
import os
import json

response =[]
print "Content-type: application/json\n\r\n\r"

#print [x for x in os.listdir('.') if x.endswith('.js')]
for x in os.listdir('./games'):
   if(os.path.isdir('./games/'+x)): 
#	print x
        if os.path.isfile('./games/'+x+'/meta.json'):
	    with open('./games/'+x+'/meta.json') as f:
    	        data = json.load(f)
                data["fname"]="/games/"+x
        	response.append(data)
#encode python array to json object for web
print(json.JSONEncoder().encode(response))
