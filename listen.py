import socket
import sys
import mmap
import time


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('0.0.0.0', 5000)
sock.bind(server_address)

sock.listen(1)
f = open('log.txt','wa+')

f.write('waiting for a connection\n')
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
                if 'field0' in data:
                        connection.send(field0)
						connection.send("\n")
                        f.write(time.time())
                        f.write('f0 sent\n')
                if 'field1' in data:
                        connection.send(field1)
						connection.send("\n")
                        f.write(time.time())
                        f.write('f1 sent\n')
                if 'field2' in data:
   #                    print >>sys.stderr, 'field 2'
                        connection.send(field2)
						connection.send("\n")
                        f.write(time.time())
                        f.write('f2 sent\n')
                if 'field5' in data:
                        connection.send(field5)
						connection.send("\n")
                        f.write(time.time())
                        f.write('f5 sent\n')
                if 'field6' in data:
     #                  print >>sys.stderr, 'field6'
                        connection.send(field6)
						connection.send("\n")
                        f.write(time.time())
                        f.write('f6 sent\n')
                if 'field7' in data:
      #                 print >>sys.stderr, 'field 7'
                        connection.send(field7)
						connection.send("\n")
                        f.write(time.time())
                        f.write('f7 sent\n')
                else
                        f.write(time.time())
                        f.write('error in request\n')
						connection.send("error invalid selection\n")
                time.sleep(1)
except KeyboardInterrupt:
        if connection:
                connection.close()
                sock.close()
		
