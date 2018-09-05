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
	with open('memmap.txt','r+') as a:
                mm = mmap.mmap(a.fileno(),0)
                field0 = mm[:5]
                field1 = mm[6:11]
                field2 = mm[12:17]
                field5 = mm[18:23]
                field6 = mm[24:29]
                field7 = mm[30:35]
	        	avgt = mm[36:]

                field0 = field0 + '\n'
                field1 = field1 + '\n'
                field2 = field2 + '\n'
                field5 = field5 + '\n'
                field6 = field6 + '\n'
                field7 = field7 + '\n'
                
        while True:
                data = connection.recv(16)
                if 'field0' in data:
                        connection.send(field0)
                        f.write(time.time())
                        f.write('f0 sent\n')
                elif 'field1' in data:
                        connection.send(field1)
                        f.write(time.time())
                        f.write('f1 sent\n')
                elif 'field2' in data:
                        connection.send(field2)
                        f.write(time.time())
                        f.write('f2 sent\n')
                elif 'field5' in data:
                        connection.send(field5)
                        f.write(time.time())
                        f.write('f5 sent\n')
                elif 'field6' in data:
                        connection.send(field6)
                        f.write(time.time())
                        f.write('f6 sent\n')
                elif 'field7' in data:
                        connection.send(field7)
                        f.write(time.time())
                        f.write('f7 sent\n')
                else:
                        f.write(time.time())
                        f.write('error in request\n')
						connection.send("error invalid selection\n")
                time.sleep(1)
except KeyboardInterrupt:
        if connection:
                connection.close()
                sock.close()
		
