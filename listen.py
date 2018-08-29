import socket
import sys
import mmap
import time


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## Binding the socket to the port

server_address = ('10.78.18.43', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

sock.listen(1)


print >>sys.stderr, 'waiting for a connection'
connection, client_address = sock.accept()
try:
	print >>sys.stderr, 'connection from', client_address
	with open('memmap.txt','r+') as a:
                mm = mmap.mmap(a.fileno(),0)
                field0 = mm[:5]
                field1 = mm[6:11]
                field2 = mm[12:17]
                field5 = mm[18:23]
                field6 = mm[24:29]
                field7 = mm[30:35]
	        avgt = mm[36:]
        
        while True:
                data = connection.recv(16)
        #        print >>sys.stderr, 'recieved "%s"' % data
                if data == 'field0':
                	print >>sys.stderr, 'field 0'
                	l = connection.send(field0)
                	le = len(field0)
                	if l != le:
                	        print 'Error!!!'
                if data == 'field1':
                	print >>sys.stderr, 'field 1'
                	l = connection.send(field1)
                	le = len(field1)
                	if l != le:
                	        print 'Error!!!'
                if data == 'field2':
                	print >>sys.stderr, 'field 2'
                	l = connection.send(field2)
                	le = len(field2)
                	if l != le:
                        	print 'Error!!!'
                if data == 'field5':
               		print >>sys.stderr, 'field 5'
                	l = connection.send(field5)
                	le = len(field5)
                	if l != le:
                	        print 'Error!!!'
                if data == 'field6':
                	print >>sys.stderr, 'field6'
                	l = connection.send(field6)
                	le = len(field6)
                	if l != le:
                	        print 'Error!!!'
            	if data == 'field7':
                	print >>sys.stderr, 'field 7'
                	l = connection.send(field7)
                	le = len(field7)
                	if l != le:
                		print 'Error!!!'
		time.sleep(10)
            #	else:
            #    	print >>sys.stderr, 'no more data to send'
            #    	break
except KeyboardInterrupt:
	if connection:
		connection.close()
		sock.close()
		
