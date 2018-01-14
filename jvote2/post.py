#!/usr/bin/python
import sys
from datetime import datetime
import cgi, cgitb 
cgitb.enable() 


my_param = cgi.getfirst('vote')

print "Content-Type: text/html\n"
print my_param

f = open("voting.txt", "a+")
f.write(str(datetime.now().strftime('%H:%M:%S'))+";"+my_param+"\n")
f.close()

if __name__ == '__main__':
	#run!
	app.run()